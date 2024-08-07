import os
import collections
from pprint import pprint

AUDIO = ['mp3','wav','raw','wma','mid','midi']
VIDEO = ['mp4','mpg','mpeg','avi','mov','flv','mkv','mwv','m4v','h264']
IMAGES = ['png','jpg','jpeg','gif','svg','bmp','psd','tiff','tif']
DOCS = ['txt','pdf','csv','xls','xlsx','ods','doc','docx','html','odt','tex','ppt','pptx','log']
COMPR = ['zip','z','7z','rar','tar','gz','pkg','deb','rpm']
INSTL = ['dmg','exe','iso']

# Creating directories for where we want to store the downloaded files
BASE_PATH = os.path.join(os.path.expanduser('~'), 'Downloads')
ORGANIZER_DIR = 'Downloads Organizer'
DEST_DIRS = ['Music','Movies','Pictures','Documents','Applications','Other']

# Create the Downloads Organizer directory if it doesn't exist
organizer_path = os.path.join(BASE_PATH, ORGANIZER_DIR)
if not os.path.isdir(organizer_path):
    os.mkdir(organizer_path)

# Create the destination directories inside the Downloads Organizer directory
for d in DEST_DIRS:
    dir_path = os.path.join(organizer_path, d)
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)

# Map files from downloads folder 
files_mapping = collections.defaultdict(list)
files_list = os.listdir(BASE_PATH)

for file_name in files_list:
    if file_name != ORGANIZER_DIR:  # Exclude the Downloads Organizer directory
        file_ext = file_name.split('.')[-1]  # Get the last element after splitting
        files_mapping[file_ext].append(file_name)

pprint(files_mapping)

# Move all files with to a target destination folder in accordance with their file type
for f_ext, f_list in files_mapping.items():
    if f_ext in INSTL:
        for file in f_list:
            os.rename(os.path.join(BASE_PATH, file), os.path.join(organizer_path, 'Applications', file))
            #print(os.path.join(BASE_PATH, file))
            #print(os.path.join(organizer_path, 'Applications', file))          
    elif f_ext in AUDIO:
        for file in f_list:
            os.rename(os.path.join(BASE_PATH, file), os.path.join(organizer_path, 'Music', file))
    elif f_ext in VIDEO:
        for file in f_list:
            os.rename(os.path.join(BASE_PATH, file), os.path.join(organizer_path, 'Movies', file))
    elif f_ext in IMAGES:
        for file in f_list:
            os.rename(os.path.join(BASE_PATH, file), os.path.join(organizer_path, 'Pictures', file))
    elif f_ext in DOCS:
        for file in f_list:
            os.rename(os.path.join(BASE_PATH, file), os.path.join(organizer_path, 'Documents', file))
    else:
        for file in f_list:
            os.rename(os.path.join(BASE_PATH, file), os.path.join(organizer_path, 'Other', file))
