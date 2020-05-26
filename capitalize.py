import os

# Change working directory to user choice
dir = input('Please input the directory name: ')
os.chdir(dir)

# Makes all files uppercase
for folder in os.listdir(dir):
    old = dir + '\\' + folder
    os.rename(old,old.lower())