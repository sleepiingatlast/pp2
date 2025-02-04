import itertools

def permut():
    ex = input()
    permutations = itertools.permutations(ex)
    
    for i in permutations:
        res = ""
        
        for char in i:
            res += char
        print(res)
        
permut()  