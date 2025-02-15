def square(n):
    for i in range(n+1):
        yield i**2

n = int(input("введите число: "))
for square_of_num in square(n):
    print(square_of_num)