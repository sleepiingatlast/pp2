import os

path = input("enter the path to check: ")

if os.path.exists(path):
    print("path exists:", True)
    print("readable:", os.access(path, os.R_OK))
    print("writable:", os.access(path, os.W_OK))
    print("executable:", os.access(path, os.X_OK))
else:
    print("path exists:", False)