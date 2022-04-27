import os, shutil

sourcePATH = input('Enter source path')
destinationPATH = input('Enter destination path')

sourcePATH = sourcePATH + '/'
destinationPATH = destinationPATH + '/'

list_of_files = os.listdir(sourcePATH)

for files in list_of_files:
    shutil.copy(sourcePATH + files, destinationPATH)