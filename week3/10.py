def unique(elem):
    res = []
    
    for i in elem:
        if i not in res:
            res.append(i)
    return res

elem_cons = input().split()
elem = []
for n in elem_cons:
    elem.append(int(n))
    
print(unique(elem))
    