
from stegano import lsb

try:
    # Load the modified image with the hidden message
    image_with_message = lsb.reveal("output_image.png")

    # Retrieve the hidden message
    hidden_message = image_with_message
    print("Hidden Message:", hidden_message)

except Exception as e:
    # Handle the exception
    print(f"sorry, occurred: {e}")