import os
#create data structure to map all files within folder
import collections
#better printing
from pprint import pprint

AUDIO = ['mp3','wav','raw','wma','mid','midi']
VIDEO = ['mp4','mpg','mpeg','avi','mov','flv','mkv','mwv','m4v','h264']
IMAGES = ['png','jpg','jpeg','gif','svg','bmp','psd','tiff','tif']
DOCS = ['txt','pdf','csv','xls','xlsx','ods','doc','docx','html','odt','tex','ppt','pptx','log']
COMPR = ['zip','z','7z','rar','tar','gz','pkg','deb','rpm']
INSTL = ['dmg','exe','iso']


#creating directories for where we want to store the downloaded files

BASE_PATH = os.path.expanduser('~')
DEST_DIRS = ['Downloads Organizer']


for d in DEST_DIRS:
    dir_path = os.path.join(BASE_PATH, d)
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)

#map files from downloads folder 
DOWNLOADS_PATH = os.path.join(BASE_PATH, 'Downloads')
files_mapping = collections.defaultdict(list)
files_list = os.listdir(DOWNLOADS_PATH)




for file_name in files_list:
    file_ext = file_name.split('.')[-1]  # Get the last element after splitting
    files_mapping[file_ext].append(file_name)


pprint(files_mapping)













        