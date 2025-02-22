import re

test_cases = ["a", "ab", "abb", "abbb"]

for i in test_cases:
    if re.search("^ab{2,3}", i):
        print(f"matched: {i}")
              
    else:
        print(f"not matched: {i}")
        