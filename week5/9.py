import re

def spaces(match):
    return " " + match.group(0)

txt = input("enter the string: ")
conv = re.sub("[A-Z]", spaces, txt)

print(conv)