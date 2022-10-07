__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
import shutil
import zipfile
from pathlib import Path

def get_files_path():
    #assuming that we are either in the files directory or its parent directory
    current_dir = Path.cwd()
    if current_dir.name != 'files':
        current_dir = Path(current_dir, 'files')
    return current_dir


def clean_cache():
    files_dir = get_files_path()
    cache_dir = Path(files_dir, 'cache')
    print(cache_dir)
    if cache_dir.is_dir():
        for item in os.listdir(cache_dir):
            if Path(cache_dir, item).is_file():
                os.remove(Path(cache_dir, item))
            else:
                shutil.rmtree(Path(cache_dir, item))
    else:
        os.mkdir(cache_dir)

def cache_zip(zip_file_path, cache_path):
    print(zip_file_path)
    print(cache_path)
    with zipfile.ZipFile(zip_file_path, "r") as zip:
        zip.extractall(cache_path)

def cached_files():
    files_dir = get_files_path()
    cache_dir = Path(files_dir, 'cache')
    pre_result = list(cache_dir.iterdir())
    result = []
    for item in pre_result:
        result.append(str(item))
    return result

def find_password(file_list):
    password_text = ''
    password_path = ''
    for path in file_list:
        with open(path) as f:
            if 'pass' in f.read() or 'secret' in f.read():
                password_path = path
                break
    
    password_text = Path(password_path).read_text()
    password_text_list = password_text.split("\n")
    for item in password_text_list:
        if 'pass' in item: 
            password_string = item
    return password_string.split(" ")[1]





