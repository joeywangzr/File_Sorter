import os, shutil

IMAGES = ["jpeg", "jpg", "ai", "gif", "psd", "png", "svg", "arw"]
VIDEOS = ["mov", "mkv", "mp4"]
DOCUMENTS = ["mobi", "epub", "pages", "docx", "doc", "txt", "docx", "pdf", "pptx", "ppt", "xlsx", "csv"]
AUDIO = ["mp3"]
APPLICATIONS = ["zip", "iso", "jar", "msi", "exe", "rar", "ttf"]

# Change working directory to user choice
dir = input('Please input the directory name: ')
os.chdir(dir)

# Check number of files in the directory
num_files = len([f for f in os.listdir('.') if os.path.isfile(f)])

print("Organizing folders...")

# Continues sorting files until no more files are in the directory
while num_files <= 0:
    for folder in os.listdir(dir):

        for t in IMAGES:
            if folder == t:
                try:
                    os.mkdir('IMAGES')
                    shutil.move(dir + '\\' + folder, dir + '\\' + 'IMAGES')
                except FileExistsError:
                    shutil.move(dir + '\\' + folder, dir + '\\' + 'IMAGES')
                break

        for t in VIDEOS:
            if folder == t:
                try:
                    os.mkdir('VIDEOS')
                    shutil.move(dir + '\\' + folder, dir + '\\' + 'VIDEOS')
                except FileExistsError:
                    shutil.move(dir + '\\' + folder, dir + '\\' + 'VIDEOS')
                break

        for t in DOCUMENTS:
            if folder == t:
                try:
                    os.mkdir('DOCUMENTS')
                    shutil.move(dir + '\\' + folder, dir + '\\' + 'DOCUMENTS')
                except FileExistsError:
                    shutil.move(dir + '\\' + folder, dir + '\\' + 'DOCUMENTS')
                break

        for t in AUDIO:
            if folder == t:
                try:
                    os.mkdir('AUDIO')
                    shutil.move(dir + '\\' + folder, dir + '\\' + 'AUDIO')
                except FileExistsError:
                    shutil.move(dir + '\\' + folder, dir + '\\' + 'AUDIO')
                break

        for t in APPLICATIONS:
            if folder == t:
                try:
                    os.mkdir('APPLICATIONS')
                    shutil.move(dir + '\\' + folder, dir + '\\' + 'APPLICATIONS')
                except FileExistsError:
                    shutil.move(dir + '\\' + folder, dir + '\\' + 'APPLICATIONS')
                break
    break

print("Done.")