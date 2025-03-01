import re

string = 'there are space,comma.And dot'

x = re.sub(r"[ ,.]", ":", string)

print(x)
