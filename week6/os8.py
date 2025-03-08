import os
path = input("enter the path: ")

if os.path.exists(path):
    if os.access(path, os.W_OK):
        os.remove(path)
        print("file deleted")
    else:
        print("file isn't writable")
else:
    print("file doesn't exist")