import os

def rename_images(directory, category):
    """
    Renames image files in the specified directory with a consistent naming pattern.

    Args:
        directory (str): Path to the directory containing images.
        category (str): Category name to prefix the image file names.
        
    Example:
        If category="electronics", files will be renamed to electronics_001.jpg, electronics_002.jpg, etc.
    """
    # Ensure category is lowercase and remove spaces
    category = category.lower().replace(" ", "_")
    
    # Get a list of all image files in the directory
    allowed_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".gif")
    files = [f for f in os.listdir(directory) if f.lower().endswith(allowed_extensions)]
    
    # Sort files to maintain consistent order
    files.sort()
    
    # Rename files
    for idx, file in enumerate(files, start=1):
        # Construct new file name
        extension = os.path.splitext(file)[1]
        new_name = f"{category}_{idx:03}{extension}"
        old_path = os.path.join(directory, file)
        new_path = os.path.join(directory, new_name)
        
        # Rename the file
        os.rename(old_path, new_path)
        print(f"Renamed: {file} -> {new_name}")

    print(f"Renaming completed for category: {category}")

# Example Usage
rename_images("E:/SnapCart/dataset/train/groceries", "Groceries")
