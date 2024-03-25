# ARW File Processor

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

python process_arw.py path_to_your_folder

Replace path_to_your_folder with the actual path to your folder.

Keeping the Terminal Window Open

## On Windows

If you're running the script from a file explorer and wish the command prompt window to remain open after the script execution, follow these steps:

1. Create a batch file (e.g., run_script.bat) in the same directory as your Python script.
2. Edit the batch file to include:

@echo off
python path\to\process_arw.py path_to_your_folder
pause

Replace path\to\process_arw.py with the path to the script and path_to_your_folder with the path to your folder.

3. Double-click the batch file to run your script. The command prompt window will remain open with a "Press any key to continue..." message after the script completes.

## On Unix/Linux/macOS

After running the script from the terminal, the window should remain open. If you're using a shortcut or script, you can append ; read -p "Press enter to continue" to the command:

python path/to/process_arw.py path_to_your_folder; read -p "Press enter to continue"

## Contributing

Feel free to fork this repository and submit pull requests to contribute to the development of this script.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
