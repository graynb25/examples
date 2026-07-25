# 🌤️ Weather App

A desktop weather application built with **Python** and **PyQt5** that retrieves real-time weather information using the OpenWeatherMap API.

## Features

- Search weather by city
- Current temperature in Fahrenheit and Celsius
- Weather description
- Weather emoji based on conditions
- Minimum and maximum temperatures
- Live local time for the selected city
- Error handling for invalid cities and network issues

## Screenshots

(Add screenshots here)

## Requirements

- Python 3.14+
- OpenWeatherMap API Key

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/weather-app.git
cd weather-app
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project folder:

```text
OPENWEATHER_API_KEY=YOUR_API_KEY_HERE
```

Run the application:

```bash
python weather.py
```

## Project Structure

```
WeatherApp/
│
├── weather.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## Technologies Used

- Python 3.14
- PyQt5
- Requests
- python-dotenv
- OpenWeatherMap API

## License

This project is licensed under the MIT License.
