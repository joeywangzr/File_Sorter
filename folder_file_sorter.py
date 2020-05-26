# Import necessary directories
import os, shutil

print('Junk file sorter')
try:
    # Change working directory to user choice
    dir = input('Please input the name of the directory you would like to sort: ')
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
    while True:
        folderSort = input('Would you like your folders to be sorted into categories? y/n ')
        if folderSort.lower() == 'y':
            
            IMAGES = ["jpeg", "jpg", "ai", "gif", "psd", "png", "svg", "arw"]
            VIDEOS = ["mov", "mkv", "mp4"]
            DOCUMENTS = ["mobi", "epub", "pages", "docx", "doc", "txt", "docx", "pdf", "pptx", "ppt", "xlsx", "csv"]
            AUDIO = ["mp3"]
            APPLICATIONS = ["zip", "iso", "jar", "msi", "exe", "rar", "ttf"]

            # Check number of files in the directory
            num_files = len([f for f in os.listdir('.') if os.path.isfile(f)])

            print("Organizing folders...")

            # Continues sorting files until no more files are in the directory
            while num_files == 0:
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

            print("All folders have been organized.")
            break

        elif folderSort.lower() == 'n':
            print('Terminating program...')
            print('Thank you for using the file sorter created by @joeywangzr.')
            break
        else:
            print('Please input either y or n.')

except FileNotFoundError:
    print('Directory not found. Please input a valid directory: ')