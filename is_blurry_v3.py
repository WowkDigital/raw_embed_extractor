import cv2
import os
import sys
import shutil
import logging

def setup_logging():
    """Konfiguracja logowania."""
    logging.basicConfig(filename='image_sorting.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    # Konfiguracja dodatkowego loggera dla wartości Laplacian var
    laplacian_logger = logging.getLogger('LaplacianLogger')
    laplacian_logger.setLevel(logging.INFO)
    handler = logging.FileHandler('laplacian_values.log')
    formatter = logging.Formatter('%(message)s')
    handler.setFormatter(formatter)
    laplacian_logger.addHandler(handler)
    return laplacian_logger

def is_blurry(image_path, threshold=100, laplacian_logger=None):
    """Funkcja do sprawdzania, czy obraz jest nieostry."""
    image = cv2.imread(image_path)
    if image is None:
        logging.info(f"Nie można załadować obrazu: {image_path}")
        return False
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()
    logging.info(f"Obraz: {image_path}, Wariancja Laplasjanu: {laplacian_var}")
    if laplacian_logger:
        laplacian_logger.info(f"{image_path}; {laplacian_var}")
    return laplacian_var < threshold

def sort_images(directory_path, threshold=100):
    """Funkcja do sortowania obrazów na nieostre i ostre."""
    blurry_dir = os.path.join(directory_path, "blurry photos")
    good_dir = os.path.join(directory_path, "good photos")

    # Tworzenie katalogów, jeśli nie istnieją
    os.makedirs(blurry_dir, exist_ok=True)
    os.makedirs(good_dir, exist_ok=True)

    laplacian_logger = setup_logging()

    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if os.path.isfile(file_path):
            if is_blurry(file_path, threshold, laplacian_logger):
                shutil.copy(file_path, os.path.join(blurry_dir, filename))
                logging.info(f"Przekopiowano do nieostre: {filename}")
            else:
                shutil.copy(file_path, os.path.join(good_dir, filename))
                logging.info(f"Przekopiowano do ostre: {filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Użycie: python script.py ścieżka_do_folderu")
        sys.exit(1)
    
    folder_path = sys.argv[1]
    if not os.path.isdir(folder_path):
        print("Podana ścieżka nie jest katalogiem.")
        sys.exit(1)

    sort_images(folder_path, threshold=300)  # Domyślny próg ustawiony na 300
    print("Zdjęcia zostały posortowane. Szczegóły w pliku 'image_sorting.log'.")
