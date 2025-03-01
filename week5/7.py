import re

def to_upper(match):
    return match.group(0).upper()

txt = input("введите строку на англ: ")
conv = re.sub(r"([a-z])+", to_upper, txt)

print(conv)