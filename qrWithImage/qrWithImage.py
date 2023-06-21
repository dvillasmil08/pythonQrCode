import qrcode
from PIL import Image

def generate_qr_code_with_image(data, image_path, file_path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    qr_image = qr.make_image(fill_color="black", back_color="white")

    # Open the image file
    overlay_image = Image.open(image_path)

    # Calculate the position to center the overlay image
    image_width, image_height = overlay_image.size
    qr_width, qr_height = qr_image.size
    position = ((qr_width - image_width) // 2, (qr_height - image_height) // 2)

    # Paste the overlay image onto the QR code image
    qr_image.paste(overlay_image, position)

    qr_image.save(file_path)

# Example usage
data = "Hello, World!"  # The data you want to encode in the QR code
image_path = "overlay_image.png"  # The path to the overlay image
file_path = "../qr_code_with_image.png"  # The path where you want to save the QR code image with the overlay

generate_qr_code_with_image(data, image_path, file_path)