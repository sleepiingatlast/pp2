import re

def to_snake(match):
    return match.group(0).lower()

txt = input("введите строку: ")
conv = re.sub(r"([A-Z])+", to_snake, txt)

print(conv)