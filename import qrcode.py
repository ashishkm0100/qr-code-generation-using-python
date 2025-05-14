import qrcode

website_link = 'https://www.linkedin.com/in/ashish-km-30124b340/'

qr = qrcode.QRCode(version=5, box_size=10, border=2)
qr.add_data(website_link)
qr.make()

img = qr.make_image(fill_color='black', back_color='red')
img.save('Here is your QR code .png')
print('Sucessfully created QR code')