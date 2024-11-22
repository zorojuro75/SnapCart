import cv2
import os

def resize_and_save_images(input_folder, output_folder, target_size=(224, 224)):
    """
    Resize all images in the input folder and save them to the output folder.

    Args:
        input_folder (str): Path to the folder containing original images.
        output_folder (str): Path to the folder to save resized images.
        target_size (tuple): Desired size for the resized images (width, height).
    """
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Get a list of all files in the input folder
    allowed_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".gif")
    files = [f for f in os.listdir(input_folder) if f.lower().endswith(allowed_extensions)]
    
    # Process each image file
    for file in files:
        input_path = os.path.join(input_folder, file)
        output_path = os.path.join(output_folder, file)

        # Read the image
        image = cv2.imread(input_path)
        if image is None:
            print(f"Skipping invalid file: {file}")
            continue

        # Resize the image
        resized_image = cv2.resize(image, target_size, interpolation=cv2.INTER_AREA)

        # Save the resized image to the output folder
        cv2.imwrite(output_path, resized_image)
        print(f"Resized and saved: {output_path}")
    
    print("All images have been resized and saved.")

# Example usage
input_folder = "E:/SnapCart/dataset/train/electronics"
output_folder = "E:/SnapCart/dataset/train/electronics_resized"
resize_and_save_images(input_folder, output_folder)
