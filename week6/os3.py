import os

path = input("enter the path: ")

if os.path.exists(path):
    print("path exists:", True)
    print("directory portion:", os.path.dirname(path))
    print("filename portion:", os.path.basename(path))
else:
    print("path exists:", False)