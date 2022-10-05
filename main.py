__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
import shutil
import zipfile
import pathlib

def clean_cache():
    current_dir = os.getcwd()
    cache_dir = current_dir + '\\files\cache'
    print(cache_dir)
    if os.path.exists(cache_dir):
        for item in os.listdir(cache_dir):
            if os.path.isfile(cache_dir +"\\"+ item):
                os.remove(cache_dir +"\\"+ item)
            else:
                shutil.rmtree(cache_dir +"\\"+ item)
    else:
        os.mkdir(cache_dir)

def cache_zip(zip_file_path, cache_path):
    print(zip_file_path)
    print(cache_path)
    with zipfile.ZipFile(zip_file_path, "r") as zip:
        zip.extractall(cache_path)

def cached_files():
    path = "C:\\Users\\majer\\Documents\\Winc\\files\\cache"
    p = pathlib.Path(path)
    pre_result = list(p.iterdir())
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
    
    password_text = pathlib.Path(password_path).read_text()
    password_text_list = password_text.split("\n")
    for item in password_text_list:
        if 'pass' in item: 
            password_string = item
    return password_string.split(" ")[1]

"""
clean_cache()
zip_file_path = "C:\\Users\\majer\\Documents\\Winc\\files\\data.zip"
cache_path = "C:\\Users\\majer\\Documents\\Winc\\files\\cache"
cache_zip(zip_file_path, cache_path)
file_path_list = (cached_files())
password = find_password(file_path_list)
print(password)
"""