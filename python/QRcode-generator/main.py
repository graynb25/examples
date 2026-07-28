import qrcode

url = input("Enter URL: ").strip()
file_path = "C:\\Users\\"Your User"\\OneDrive\\Desktop\\qrcode.png"

qr = qrcode.QRCode()
qr.add_data(url)


img = qr.make_image()
img.save(file_path)

print("QR Code Generated")
