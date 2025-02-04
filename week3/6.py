def rev(ex):
    words = ex.split()
    words.reverse()
    
    res = ""
    
    for i in words:
        res += i + " "
    return res.strip()

ex = input()
print(rev(ex))