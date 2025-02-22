import re

test_cases = ["a", "ab", "abb", "ac"]

for s in test_cases:
    if re.search(r"^ab*", s):
        print(f"matched: {s}")
    else: 
        print(f"not matched: {s}")