# Import necessary directories
import os, shutil

# Change working directory to user choice
dir = input('Please input a directory name: ')
os.chdir(dir)

print('Sorting files...')

# Check number of files in the directory
num_files = len([f for f in os.listdir('.') if os.path.isfile(f)])

# Continues sorting files until no more files are in the directory
while num_files > 0:
# Loops through all files in the working directory
    for file in os.listdir(dir):
# Checks if "file" is a file
# Confirmed that "file" is a file
        if '.' in file:
            file = file[::-1]
# Isolates file type
            fileType = file[0:file.index('.')]
            fileType = fileType[::-1]
            file = file[::-1]
# Creates a new folder for that file type
            try:
                os.mkdir(dir + '\\' + fileType)
# Move file into corresponding folder
                shutil.move(dir + '\\' + file, dir + '\\' + fileType)
# If folder for that file type exists, do not create new folder; move to existing folder
            except FileExistsError:
                shutil.move(dir + '\\' + file, dir + '\\' + fileType)

# "file" is not a file
        else:
# If files are left in the directory, the code continues to run
            if num_files > 0:
                continue
# If no more files are remaining, the code stops running
            elif num_files == 0:
                break
    break

print('All files have been sorted!')