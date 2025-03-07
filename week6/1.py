def mult_all_nums(nums):
    res = 1
    
    for i in nums:
        res *= i
    return res

nums = list(map(int, input("введите числа: ").split()))
res = mult_all_nums(nums)
print("ваш результат:", res)