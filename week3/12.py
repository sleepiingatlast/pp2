def histogram(nums):
    for i in nums:
        print("*" * i)
        
ex = input().split()
nums = []
for n in ex:
    nums.append(int(n))
    
histogram(nums)