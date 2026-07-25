# Python Weather API app

import sys
import requests
import os
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QLineEdit, QPushButton, QVBoxLayout)

from PyQt5.QtCore import QTimer, Qt
from datetime import datetime, timezone, timedelta
from dotenv import load_dotenv

load_dotenv()

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter City Name", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.minmax_temperature_label = QLabel(self)
        self.time_label = QLabel(self)
        self.feels_like_label = QLabel(self)
        self.humidity_label = QLabel(self)
        self.wind_label = QLabel(self)
        self.visibility_label = QLabel(self)
        self.sunrise_label = QLabel(self)
        self.sunset_label = QLabel(self)
        self.timer = QTimer(self)
        self.weather_data = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Weather App")

        vbox = QVBoxLayout()

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)
        vbox.addWidget(self.minmax_temperature_label)
        vbox.addWidget(self.feels_like_label)
        vbox.addWidget(self.humidity_label)
        vbox.addWidget(self.wind_label)
        vbox.addWidget(self.visibility_label)
        vbox.addWidget(self.sunrise_label)
        vbox.addWidget(self.sunset_label)
        vbox.addWidget(self.time_label)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.city_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.description_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.minmax_temperature_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.feels_like_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.humidity_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.wind_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.visibility_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sunrise_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sunset_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")
        self.minmax_temperature_label.setObjectName("minmax_temperature_label")
        self.feels_like_label.setObjectName("feels_like_label")
        self.humidity_label.setObjectName("humidity_label")
        self.wind_label.setObjectName("wind_label")
        self.visibility_label.setObjectName("visibility_label")
        self.sunrise_label.setObjectName("sunrise_label")
        self.sunset_label.setObjectName("sunset_label")
        self.time_label.setObjectName("time_label")

        self.setStyleSheet("""
            QLabel, QPushButton{
                font-family: Roboto, sans-serif;
            }
            QLabel#city_label{
                font-size: 40px;
                font-style: bold;
            }
            QLineEdit#city_input{
                font-size: 40px;
            }
            QPushButton#get_weather_button{
                font-size: 30px;
                font-weight: bold;
            }
            QLabel#temperature_label{
                font-size: 55px;
            }
            QLabel#emoji_label{
                font-size: 100px;
                font-family: Segoe UI Emoji;
            }
            QLabel#description_label{
                font-size: 40px;
                font-weight: bold;
            }
            
            QLabel#minmax_temperature_label{
                font-size: 20px;
                font-weight: bold;
            }
            QLabel#time_label{
                font-size: 20px;
                font-weight: bold;
            }
            QLabel#feels_like_label{
                font-size: 15px;
                font-weight: bold;
            }
            QLabel#humidity_label{
                font-size: 15px;
                font-weight: bold;
            }
            QLabel#wind_label{
                font-size: 15px;
                font-weight: bold;
            }
            QLabel#visibility_label{
                font-size: 15px;
                font-weight: bold;
            }
            QLabel#sunrise_label{
                font-size: 15px;
                font-weight: bold;
            }
            QLabel#sunset_label{
                font-size: 15px;
                font-weight: bold;
            }
            
        """)

        self.get_weather_button.clicked.connect(self.get_weather)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)


    def get_weather(self):

        api_key = os.getenv("OPENWEATHER_API_KEY")
        city = self.city_input.text().strip()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()

            if int(data["cod"]) == 200:
                self.display_weather(data)

        except requests.exceptions.HTTPError as http_error: # HTTP errors
            match response.status_code:
                case 400:
                    self.display_error("Bad Request:\nPlease check your input")
                case 401:
                    self.display_error("Unauthorized:\nInvalid API Key")
                case 403:
                    self.display_error("Forbidden:\nAccess is denied")
                case 404:
                    self.display_error("Not Found:\nCity not found")
                case 500:
                    self.display_error("Internal Server Error:\nPlease try again later")
                case 502:
                    self.display_error("Bad Gateway:\nInvalid response from the server")
                case 503:
                    self.display_error("Service Unavailable:\nServer is down")
                case 504:
                    self.display_error("Gateway Timeout:\nNo response from the server")
                case _:
                    self.display_error(f"HTTP error occurred:\n{http_error}")

        except requests.exceptions.ConnectionError: # network problems, invalid URLs
            self.display_error("Connection Error\nPlease check your internet connection")
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error\nThe request timed out")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many Redirects\nCheck the url")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error\n{req_error}")

    def display_error(self, message):

        self.city_label.setText("Enter City Name")
        self.city_label.setText(self.city_input.text().strip())
        self.temperature_label.setStyleSheet("font-size: 20px;")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()
        self.minmax_temperature_label.clear()
        self.time_label.clear()
        self.city_input.clear()
        self.feels_like_label.clear()
        self.humidity_label.clear()
        self.wind_label.clear()
        self.visibility_label.clear()
        self.sunrise_label.clear()
        self.sunset_label.clear()

    def display_weather(self, data):
        self.weather_data = data

        self.temperature_label.setStyleSheet("font-size: 40px;")
        self.minmax_temperature_label.setStyleSheet("font-size: 15px;")
        self.time_label.setStyleSheet("font-size: 15px;")
        temperature_k = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        visibility = data["visibility"]
        sunrise = data["sys"]["sunrise"]
        sunset = data["sys"]["sunset"]
        temperature_c = temperature_k - 273.15
        temperature_f = (temperature_k * 9/5) - 459.67
        weather_id = data["weather"][0]["id"]
        weather_desc = data["weather"][0]["description"].capitalize()
        temperature_min = data["main"]["temp_min"]
        temperature_max = data["main"]["temp_max"]
        temp_min_c = temperature_min - 273.15
        temp_max_c = temperature_max - 273.15
        temp_min_f = (temperature_min * 9 / 5) - 459.67
        temp_max_f = (temperature_max * 9 / 5) - 459.67
        feels_c = feels_like - 273.15
        feels_f = (feels_like * 9 / 5) - 459.67
        wind_mph = wind_speed * 2.237
        wind_kmh = wind_speed * 3.6
        visibility_miles = visibility / 1609.34
        visibility_km = visibility / 1000
        city_name = data["name"]
        country = data["sys"]["country"]

        self.temperature_label.setText(f"{temperature_f:.0f}°F  |  {temperature_c:.0f}°C")
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description_label.setText(f"{weather_desc}")
        self.minmax_temperature_label.setText(f"Min: {temp_min_f:.0f}°F / Max: {temp_max_f:.0f}°F"
                                              f"  |  Min: {temp_min_c:.0f}°C / Max: {temp_max_c:.0f}°C")

        offset = timezone(timedelta(seconds=data["timezone"]))
        sunrise_time = datetime.fromtimestamp(sunrise,offset).strftime("%I:%M %p")
        sunset_time = datetime.fromtimestamp(sunset,offset).strftime("%I:%M %p")

        self.feels_like_label.setText(
            f"Feels Like: {feels_f:.0f}°F | {feels_c:.0f}°C")
        self.humidity_label.setText(f"Humidity: {humidity}%")
        self.wind_label.setText(f"Wind: {wind_mph:.1f} mph | {wind_kmh:.1f} km/h")
        self.visibility_label.setText(f"Visibility: {visibility_miles:.1f} mi | {visibility_km:.1f} km")
        self.sunrise_label.setText(f"🌅 Sunrise: {sunrise_time}")
        self.sunset_label.setText(f"🌇 Sunset: {sunset_time}")
        self.city_label.setText(f"{city_name}, {country}")


        self.update_time()

    def update_time(self):
        if not self.weather_data:
            self.time_label.setText("Search a city to see local time")
            return

        offset = timedelta(seconds=self.weather_data["timezone"])
        city_time = datetime.now(timezone(offset))

        self.time_label.setText(city_time.strftime("%I:%M:%S %p"))

    @staticmethod
    def get_weather_emoji(weather_id):

        if 200 <= weather_id <= 232:
            return "⛈️"
        elif 300 <= weather_id <= 321:
            return "🌦️️"
        elif 500 <= weather_id <= 531:
            return "🌧️"
        elif 600 <= weather_id <= 622:
            return "❄️"
        elif 701 <= weather_id <= 741:
            return "🌫️"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "💨"
        elif weather_id == 781:
            return "🌪️"
        elif weather_id == 800:
            return "☀️"
        elif 801 <= weather_id <= 804:
            return "☁️"
        else:
            return ""


if __name__ == '__main__':
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
