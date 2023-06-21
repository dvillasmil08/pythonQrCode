import qrcode
from PIL import Image


def generate_round_qr_code_with_image(data, image_path, file_path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=8,  # Increase the box_size value for larger images
        border=1,  # Reduce the border value for less boxy edges
    )
    qr.add_data(data)
    qr.make(fit=True)

    qr_image = qr.make_image(fill_color="black", back_color="white")

    # Open the overlay image
    overlay_image = Image.open(image_path)

    # Resize the overlay image to fit within the QR code while maintaining aspect ratio
    qr_width, qr_height = qr_image.size
    max_size = max(qr_width, qr_height)
    overlay_image.thumbnail((max_size, max_size))

    # Calculate the position to center the overlay image
    position = ((qr_width - overlay_image.width) // 2, (qr_height - overlay_image.height) // 2)

    # Create a new image with RGBA mode
    qr_with_overlay = qr_image.convert("RGBA")

    # Paste the overlay image onto the QR code image using alpha blending
    qr_with_overlay.paste(overlay_image, position, overlay_image)

    # Save the QR code image with the overlay
    qr_with_overlay.save(file_path)


# Example usage
data = "https://dvillasmil08.github.io/dvillasmil/"  # The data you want to encode in the QR code
image_path = "Shock100.png"  # The path to the overlay image
file_path = "qr_code_with_image.png"  # The path where you want to save the QR code image with the overlay

generate_round_qr_code_with_image(data, image_path, file_path)
