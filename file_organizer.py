from os import scandir, rename
from os.path import splitext, exists, join
from shutil import move   #To move file form one folder to another
from time import sleep    #To pasue the program for some time 
import logging #Used to log messages (like info, warning, and error messages) 
from watchdog.observers import Observer  #Watchers for changes in the netowork and trigger chages 
from watchdog.events import FileSystemEventHandler #It responds to file system events live file creation, deletion etc.
import time

# Folder to track (source) and destination folders for different file types
source_dir = "D:\\New Downloads"
dest_dirs = {
    "music": "D:\\New Downloads",
    "video": "D:\\New Downloads",
    "image": "D:\\New Downloads\\New_Donwloads_Images",
    "documents": "D:\\New Downloads\\New_Donwloads_PDF",
    "python": "D:\\New Downloads\\New_Donwloads_Python"
}

# Supported file extensions for different categories
file_types = {
    "image": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".ico"],
    "video": [".mp4", ".avi", ".mkv", ".mov"],
    "audio": [".mp3", ".wav", ".flac"],
    "document": [".doc", ".pdf", ".xls", ".ppt", ".csv"],
    "python": [".py"]
}

# Make the filename unique if it already exists in the destination directory
def make_unique(dest, name):
    filename, extension = splitext(name)
    counter = 1
    while exists(f"{dest}/{name}"):
        name = f"{filename}({counter}){extension}"
        counter += 1
    return name

# Move file to the destination, with retries if the file is in use
def move_file(dest, entry, name, retries=3, delay=1):
    for i in range(retries):
        try:
            if exists(f"{dest}/{name}"):
                name = make_unique(dest, name)
            move(entry, dest)  # Moves file from source to destination
            logging.info(f"Moved file: {name}")
            return
        except PermissionError:
            logging.warning(f"Attempt {i+1}: {name} is in use. Retrying in {delay} seconds.")
            time.sleep(delay)
    logging.error(f"Failed to move {name} after {retries} attempts: File is still in use.")

# Handler for processing file events
class MoverHandler(FileSystemEventHandler):
    # This method is triggered whenever a file change is detected
    def on_modified(self, event):
        with scandir(source_dir) as entries:
            for entry in entries:
                self.categorize_and_move(entry)

    # Categorize files based on extension and move them
    def categorize_and_move(self, entry):
        name = entry.name
        for category, extensions in file_types.items():
            if any(name.lower().endswith(ext) for ext in extensions):
                move_file(dest_dirs[category], entry, name)
                break

# Main execution
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    event_handler = MoverHandler()
    observer = Observer()
    observer.schedule(event_handler, source_dir, recursive=True)
    observer.start()
    try:
        while True:
            sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
