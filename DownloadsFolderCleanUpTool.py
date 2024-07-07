import os


AUDIO = ['mp3','wav','raw','wma','mid','midi']
VIDEO = ['mp4','mpg','mpeg','avi','mov','flv','mkv','mwv','m4v','h264']
IMAGES = ['png','jpg','jpeg','gif','svg','bmp','psd','tiff','tif']
DOCS = ['txt','pdf','csv','xls','xlsx','ods','doc','docx','html','odt','tex','ppt','pptx','log']
COMPR = ['zip','z','7z','rar','tar','gz','pkg','deb','rpm']
INSTL = ['dmg','exe','iso']


#creating directories 

BASE_PATH = os.path.expanduser('~')
DEST_DIRS = ['tester folder']


for d in DEST_DIRS:
    dir_path = os.path.join(BASE_PATH, d)
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)














        