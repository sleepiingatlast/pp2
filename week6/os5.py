file_path = input("enter the file path: ")
my_list = ["apple", "banana", "cherry", "date"]

with open(file_path, 'w') as file:
    for item in my_list:
        file.write(item + '\n')

print("list written to file")