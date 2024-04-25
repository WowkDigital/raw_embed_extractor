import os
import sys
import rawpy
import io
from PIL import Image, ExifTags

def rotate_image_based_on_exif(image):
    try:
        exif = {
            ExifTags.TAGS[k]: v
            for k, v in image._getexif().items()
            if k in ExifTags.TAGS
        }

        orientation = exif.get('Orientation')
        if orientation == 3:
            image = image.rotate(180, expand=True)
        elif orientation == 6:
            image = image.rotate(270, expand=True)
        elif orientation == 8:
            image = image.rotate(90, expand=True)
    except Exception as e:
        print(f"Error processing EXIF data: {e}")
    return image

def process_image(raw_file_path, jpg_folder_path):
    with rawpy.imread(raw_file_path) as raw:
        embedded_image = raw.extract_thumb()
        if embedded_image.format == rawpy.ThumbFormat.JPEG:
            img = Image.open(io.BytesIO(embedded_image.data))
            img = rotate_image_based_on_exif(img)
            final_path = os.path.join(jpg_folder_path, os.path.splitext(os.path.basename(raw_file_path))[0] + '.jpg')
            img.save(final_path)
            print(f"Saved and rotated JPG preview at: {final_path}")
        else:
            print("Embedded JPG image not found in RAW file.")

def process_raw_folder(folder_path):
    jpg_folder_path = os.path.join(folder_path, 'jpg')
    if os.path.exists(jpg_folder_path):
        # Find a unique folder name if the default exists
        suffix = 1
        while os.path.exists(f"{jpg_folder_path}_{suffix}"):
            suffix += 1
        jpg_folder_path = f"{jpg_folder_path}_{suffix}"
    os.makedirs(jpg_folder_path)
    
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.arw', '.cr2')):
            process_image(os.path.join(folder_path, filename), jpg_folder_path)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: script.py <folder_path>")
        print("The script converts ARW and CR2 raw images to JPG in a new directory within the specified folder path.")
        print("If the 'jpg' folder exists, a new unique folder will be created to avoid overwriting existing files.")
        sys.exit(1)
    folder_path = sys.argv[1]
    process_raw_folder(folder_path)
    if os.name == 'nt':
        os.system("pause")
    else:
        input("Press enter to continue...")
