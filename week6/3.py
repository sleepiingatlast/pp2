def palindrome(txt):
    txt2 = "".join(reversed(txt))
    
    if txt.lower() == txt2.lower():
        print("its palindrome")
    else:
        print("its not palindrome")
        
txt = input("enter a string to check: ")
palindrome(txt)