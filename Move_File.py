import os
import shutil

a=os.getcwd()
print('The Path of the File is', a)
 
path=os.path.exists('C:/Users/Windows 10/OneDrive/Desktop')
print(path)
source='C:/Users/Windows 10/Downloads'
destination='C:/Users/Windows 10/OneDrive/Desktop'
files=os.listdir(source)
for i in files:
    name,ext=os.path.splitext(i)
    if(ext==''):
        continue
    if ext in ['.txt', '.doc', '.docx', '.pdf',]:
        path1 = source + '/' + i
        path2 = destination + '/' + 'Document_Files'
        path3 = destination + '/' + 'Document_Files' + '/' + i

        if os.path.exists(path2):
            print('folder already exists and moving the files')
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print('Creating folder and moving the files')
            shutil.move(path1,path3)