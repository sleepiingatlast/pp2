import math
num_of_sides= int(input("введите кол-во сторон фигуры: "))
len_of_side = int(input("введите сторону фигуры: "))

area = int((num_of_sides * len_of_side**2) / (4 * math.tan(math.radians(180) / num_of_sides))
)
print(area)