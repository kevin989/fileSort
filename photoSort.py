
from PIL import Image
from pathlib import Path
import shutil
from datetime import datetime as dt
import os

#Steps
#1. iterate over each photo in a folder
#2. get photo metadata
#3. get date from metadata of the files in the folder 
#       --and subfolders
#4. If there is no folder for the year, create one
#5. If there is no subfolder for the month, create one
#else, move the file to the abs path of the subfolder
#6. Continue for next file until no more files

#1. iterate over each files in folder & 2. get metadata

def get_meta(file):
    supported_type = ['.BLP', '.JPG', '.BMP', '.DDS', '.DIB', '.EPS', '.GIF', 
    '.ICNS', '.ICO', '.PNG', '.TIFF', '.WEBP']
    if file.is_file() and file.suffix.upper() in supported_type:
        with Image.open(file) as im:
            meta_data = im.getexif()
    return(meta_data)


def get_date(path):
    folder_path = Path(path)
    for file in folder_path.iterdir():
        meta_data = get_meta(file)
        try:
            orig_date, orig_time = meta_data[306].split(" ") #306 is the key for 'datetime'
            year, month, day = orig_date.split(":")
            check_folder = folder_path.joinpath(year)
            if not check_folder.exists():
                check_folder.mkdir()
        except KeyError:
                continue
    print(year, month)

get_date("C:\\Users\\Kevin\\Pictures")

