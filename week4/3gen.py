def square(n):
    for i in range(n+1):
        yield i
    
n = int(input("введите число: "))

for num in square(n):
    if num % 3 == 0 and num % 4 == 0:
        print(num)