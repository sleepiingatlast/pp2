def all_true(tup):
    return all(tup)

my_tuple = (True, 1, "Hello", [1, 2], 3.5)  
print(all_true(my_tuple))  

my_tuple2 = (True, 1, "", 3)  
print(all_true(my_tuple2)) 