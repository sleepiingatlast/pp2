import re

string = 'aaab daaad a45b'
x = re.search("a.+?b", string)

print(x)