def squares(a, b):
    for i in range(a, b+1):
        yield i
        
a = int(input("введите а: "))
b = int(input("введите b: "))

for num in squares(a, b):
    print(num)