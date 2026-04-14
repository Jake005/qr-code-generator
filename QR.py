import qrcode

# Replace the url with the desired url
url = "https://www.youtube.com/"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(url)
qr.make(fit=True)


img = qr.make_image(fill_color="black", back_color="white")

# From here you can change the name of the generated qr code.
img.save("qr_code.png")

print("QR code generated and saved as qr_code.png")