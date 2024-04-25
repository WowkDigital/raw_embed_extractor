import os
import sys
import rawpy
import io
from PIL import Image, ExifTags

def rotate_image_based_on_exif(image):
    try:
        exif = image.getexif()  # Changed from _getexif to getexif
        exif = {
            ExifTags.TAGS.get(k, k): v
            for k, v in exif.items()
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

def process_image(raw_file_path, output_file):
    with rawpy.imread(raw_file_path) as raw:
        embedded_image = raw.extract_thumb()
        if embedded_image.format == rawpy.ThumbFormat.JPEG:
            img = Image.open(io.BytesIO(embedded_image.data))
            img = rotate_image_based_on_exif(img)
            img.save(output_file)
            print(f"Saved and rotated JPG preview at: {output_file}")
        else:
            print("Embedded JPG image not found in RAW file.")

def process_raw_folder(raws_dir):
    jpg_folder_path = os.path.join(raws_dir, '..', 'thumbs_jpg')
    
    if not os.path.exists(jpg_folder_path):
        os.makedirs(jpg_folder_path)
    
    for filename in os.listdir(raws_dir):
        if filename.lower().endswith(('.arw', '.cr2')):
            output_file = os.path.join(jpg_folder_path, os.path.splitext(os.path.basename(filename))[0] + '.jpg')
            if os.path.exists(output_file):
                print(f"Skipping {output_file} (it already exists)")
            else:
                process_image(os.path.join(raws_dir, filename), output_file)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        pyfile = os.path.basename(__file__)
        print(f"Usage: {pyfile} <dir with raws>")
        sys.exit(1)
    raws_dir = sys.argv[1]
    if os.path.isdir(raws_dir):
        process_raw_folder(raws_dir)
    else:
        print("Given path does not exist or is not a directory")
        sys.exit(2)
    # input("Press enter to continue...")
