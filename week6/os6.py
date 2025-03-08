import string

for letter in string.ascii_uppercase:
    open(f"{letter}.txt", 'w').close()

print("26 text files (A.txt to Z.txt) created.")