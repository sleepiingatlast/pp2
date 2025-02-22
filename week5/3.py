import re

test_cases = ["ab_c", "abc", "a__p"]

for i in test_cases:
    if(re.search(r"^[a-z]+_[a-z]+$", i)):
        print(f"matched: {i}")
              
    else:
        print(f"not matched: {i}")
        