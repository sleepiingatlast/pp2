import re

test_cases = ["Add", "DAa", "aaF"]

for i in test_cases:
    if re.search(r"^[A-Z]{1}[a-z]+$", i):
         print(f"matched: {i}")
              
    else:
        print(f"not matched: {i}")
        