import math
import time

num = int(input("введите число: "))
delay = int(input("введите задержку в мсек: "))

time.sleep(delay/1000) #ставим прогр на паузу пока не достигнем delay/1000

print(f"корень {num} после {delay} в милисекундах равен {math.sqrt(num)}")