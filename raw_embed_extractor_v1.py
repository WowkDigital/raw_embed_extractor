import os
import rawpy
import PIL
import sys
import os
from PIL import Image, ExifTags

def rotate_image_based_on_exif(image, exif_bytes):
    try:
        exif_dict = PIL.ExifTags.TAGS
        if exif_bytes:
            exif = {exif_dict[k]: v for k, v in Image.open(io.BytesIO(exif_bytes))._getexif().items() if k in exif_dict}
        else:
            exif = {}

        orientation = exif.get('Orientation')
        if orientation == 3:
            image = image.rotate(180, expand=True)
        elif orientation == 6:
            image = image.rotate(270, expand=True)
        elif orientation == 8:
            image = image.rotate(90, expand=True)
    except Exception:
        pass
    return image, exif_bytes

def extract_and_rotate_image(arw_file_path, jpg_folder_path):
    with rawpy.imread(arw_file_path) as raw:
        embedded_image = raw.extract_thumb()
        if embedded_image.format == rawpy.ThumbFormat.JPEG:
            temp_jpg_path = os.path.join(jpg_folder_path, 'temp.jpg')
            with open(temp_jpg_path, 'wb') as f:
                f.write(embedded_image.data)

            with Image.open(temp_jpg_path) as img:
                exif_bytes = img.info.get('exif', None)
                img, exif_bytes = rotate_image_based_on_exif(img, exif_bytes)
                final_path = os.path.join(jpg_folder_path, os.path.basename(arw_file_path).replace('.ARW', '.jpg'))
                img.save(final_path, exif=exif_bytes)
            os.remove(temp_jpg_path)
            print(f"Saved and rotated JPG preview at: {final_path}")
        else:
            print("Embedded JPG image not found in RAW file.")

def process_arw_folder(folder_path):
    jpg_folder_path = os.path.join(folder_path, 'jpg')
    os.makedirs(jpg_folder_path, exist_ok=True)
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.arw'):
            arw_file_path = os.path.join(folder_path, filename)
            extract_and_rotate_image(arw_file_path, jpg_folder_path)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: script.py <folder_path>")
        sys.exit(1)
    folder_path = sys.argv[1]
    process_arw_folder(folder_path)
    os.system("pause") if os.name == 'nt' else input("Press enter to continue...")