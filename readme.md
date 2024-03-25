# ARW File Processor

[raw_embed_extractor_v1.py](https://github.com/WowkDigital/raw_embed_extractor/blob/main/raw_embed_extractor_v1.py)

This Python script automates the process of extracting embedded JPG images from ARW files, rotating them based on EXIF data, preserving the EXIF metadata, and saving them to a specified directory. It is designed to work with a batch of .arw files within a folder.

## Requirements

- Python 3.x
- PIL (Pillow)
- rawpy

Ensure you have the required dependencies installed. You can install them using pip:

pip install Pillow rawpy

## Usage

Running the Script Directly

1. Open a terminal or command prompt.
2. Navigate to the directory containing the script.
3. Run the script with the path to the folder containing .arw files as an argument:

python raw_embed_extractor_v1.py path_to_your_folder

Replace path_to_your_folder with the actual path to your folder.

Keeping the Terminal Window Open

## Contributing

Feel free to fork this repository and submit pull requests to contribute to the development of this script.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
