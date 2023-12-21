from PIL import Image
import os

def compress_image(input_path, output_path, target_size_kb):
    # Open the image
    original_image = Image.open(input_path)

    # Save the image to a temporary file with reduced quality
    temp_path = "temp.jpg"
    original_image.save(temp_path, quality=85)

    # Calculate the compression ratio needed to achieve the target size
    current_size_kb = os.path.getsize(temp_path) / 1024.0
    compression_ratio = target_size_kb / current_size_kb

    # If the image is already smaller than the target size, just copy it
    if compression_ratio >= 1.0:
        original_image.save(output_path)
        os.remove(temp_path)
        return

    # Compress the image with the calculated compression ratio
    compressed_image = Image.open(temp_path)
    compressed_image.save(output_path, quality=int(85 * compression_ratio))

    # Remove the temporary file
    os.remove(temp_path)

if __name__ == "__main__":
    # Get input from the user
    input_image_path = input("Enter the path to the input image: ")
    compressed_output_path = input("Enter the path to save the compressed image: ")
    target_size_kb = float(input("Enter the target size in kilobytes: "))

    # Call the function to compress the image
    compress_image(input_image_path, compressed_output_path, target_size_kb)

    print("Image compression complete.")
