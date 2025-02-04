def prime_nums(nums):
    primes = []
    for num in nums:
        num = int(num)
        if num < 2:
            continue
        prime_nums = True
        
        for i in range(2, num):
            if num % i == 0:
                prime_nums = False
                break
        if prime_nums:
            primes.append(num)
    return primes

nums = input().split()

print(prime_nums(nums))
    