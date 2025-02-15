def nums(n):
    for i in range(n, -1, -1):
        yield i
        
n = int(input("введите число n: "))

for num in nums(n):
    print(num)