def palindrome(ex):
    txt = ""
    for i in ex.lower():
        if 'a' <= i <= 'z' or '0' <= i <= '9':
            txt += i
    return txt == ex[::-1]

s = input()
if palindrome(s):
    print("yes")
else:
    print("no")