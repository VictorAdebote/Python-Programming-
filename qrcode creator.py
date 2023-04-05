import qrcode

# Prompt the user for input
data = input('Enter the data to encode: ')

# Create a QR code instance
qr = qrcode.QRCode(version=1, box_size=10, border=5)

# Add the data to QR code
qr.add_data(data)

# Generate the Qr code
qr.make(fit=True)

# Create an image from QR code
img = qr.make_image(fill_color='Black', back_color='white')

# Save the image as PNG file
filename = input('Enter the {filename} to save the QR code as: ')

img.save(f'{filename}.png')

print(f'Qr code saves as {filename}.png')