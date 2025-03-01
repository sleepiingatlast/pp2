import re

txt = input("enter a string: ")
conv = re.split("(?=[A-Z])", txt)[1:]

print(conv)