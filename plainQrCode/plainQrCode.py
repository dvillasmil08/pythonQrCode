import qrcode

def generate_qr_code(data, file_path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=2,
    )
    qr.add_data(data)
    qr.make(fit=True)

    image = qr.make_image(fill_color="black", back_color="white")
    image.save(file_path)

# Example usage
data = "Hello, World!"  # The data you want to encode in the QR code
file_path = "../qr_code.png"  # The path where you want to save the QR code image

generate_qr_code(data, file_path)