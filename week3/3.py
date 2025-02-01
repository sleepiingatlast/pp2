def solve(numheads, numlegs):
    for num_rab in range(numheads+1): 
        num_chick = numheads - num_rab
        if 2*num_chick + 4*num_rab == numlegs:
            return num_chick, num_rab
    
print(solve(35, 94)) 