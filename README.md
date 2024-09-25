# Automated File Organizer

This Python script automates the task of organizing files in a directory by monitoring the folder and moving files to designated subfolders based on their file type (e.g., images, videos, audio, documents). 

## Project Overview

The file organizer script was developed to streamline file management by automatically sorting files in a specified folder. The script listens for changes in a target folder and moves files into categorized subfolders, based on their file extensions (e.g., `.jpg` files to an `Images` folder, `.mp4` files to a `Videos` folder). 

By leveraging Python and the Watchdog module, this script improves productivity and prevents clutter in directories where multiple types of files are frequently downloaded or stored.

## Features

- **Real-Time Monitoring**: Monitors changes in the directory (new files or modifications).
- **Automated File Organization**: Moves files into categorized subfolders (e.g., images, videos, audio, documents, and Python scripts).
- **Customizable Directory Paths**: Easily configurable source and destination directories.
- **Retry Logic**: Handles files that are in use and retries the operation automatically.
- **Supports Multiple File Types**: Predefined support for image, video, audio, document, and Python files.
- **Cross-Platform Compatibility**: Works on both Windows and Linux systems with minor path adjustments.

## Modules Used

- **os**: Used for interacting with the operating system, including functions for file renaming, moving, and checking if files exist.
- **shutil**: Provides the `move()` function to handle file moving.
- **time**: Adds delays between retries and handles the sleep functionality in the main loop.
- **logging**: Logs events, such as file moves and errors, to the console for easier debugging.
- **watchdog**: A Python library used to monitor file system changes and trigger actions accordingly.

## Setup and Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/automated-file-organizer.git
    ```

2. **Install dependencies:**

    ```bash
    pip install watchdog
    ```

3. **Configure the source and destination directories:**

    Open the script and modify the `source_dir` and destination paths inside the `dest_dirs` dictionary to your desired directories.

4. **Run the script:**

    ```bash
    python file_organizer.py
    ```

## How It Works

- The script uses the `watchdog` library to monitor the specified `source_dir`.
- Once a file is modified or added, the event handler checks the file's extension and moves it to the appropriate destination folder.
- If a file with the same name already exists in the destination folder, the script adds a numeric suffix to ensure uniqueness (e.g., `file(1).txt`).
- The script retries moving files that are in use with a delay, logging any issues or errors encountered.

## Customization

You can extend this project by:
- Adding more file types to the `file_types` dictionary.
- Changing the retry logic and delay intervals in the `move_file()` function.
- Integrating more advanced features like archiving or compression of old files.

## Contribution

Feel free to fork this repository and submit pull requests for new features or bug fixes. Any contributions are welcome!

## License

This project is licensed under the MIT License.
