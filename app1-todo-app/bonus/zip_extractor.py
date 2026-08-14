import zipfile

def extract_archive(archievepath, dest_dir):
    with zipfile.ZipFile(archievepath, 'r') as archive:
        archive.extractall(dest_dir)

if __name__ == "__main__":
    extract_archive("C:/Users/Maciej/Desktop/PROJEKTY-PYTHON/Python-podstawy/bonus/compressed.zip",
                    dest_dir="C:/Users/Maciej/Desktop/PROJEKTY-PYTHON/Python-podstawy/bonus/files")