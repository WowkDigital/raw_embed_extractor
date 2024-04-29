import os
import shutil

def select_folder():
    print("Please enter the path to the folder:")
    folder_selected = input().strip()
    return folder_selected

def copy_files(source_folder, ids):
    destination_folder = os.path.join(source_folder, "SelectedFiles")
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for filename in os.listdir(source_folder):
        if filename.endswith(".ARW"):
            file_id = filename.split('(')[-1].split(')')[0]
            if file_id in ids:
                shutil.copy2(os.path.join(source_folder, filename), destination_folder)
    print("Files copied successfully to:", destination_folder)

def main():
    print("Welcome to the File Copier script.")
    source_folder = select_folder()
    print("Enter the IDs of the files to copy, separated by commas (e.g., 123,456):")
    ids = input().strip().split(',')
    copy_files(source_folder, ids)

if __name__ == "__main__":
    main()
