def square(n):
    for i in range(0, n+1, 2):
        yield i
    
n = int(input("введите число: "))

list_of_even = []
for num in square(n):
    list_of_even.append(str(num))
    
print(", ".join(list_of_even))