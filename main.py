import qrcode

url = input("Enter the URL: ")

qr = qrcode.QRCode(
    version=1, 
    error_correction=qrcode.constants.ERROR_CORRECT_L, 
    box_size=10,  
    border=4,  
)

qr.add_data(url)

qr.make(fit=True)

img = qr.make_image(fill_color="white", back_color="black")

img.save("output.png")

print("QR code generated as output.png")
