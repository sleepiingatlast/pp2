file_path = input("enter the text file path: ")

try:
    line_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            line_count += 1
    print("number of lines:", line_count)
except FileNotFoundError:
    print("error: file not found.")