def count(txt):
    count_uppers = sum(1 for i in txt if i.isupper())
    count_lowers = sum(1 for i in txt if i.islower())
    
    print("заглавынх букв:", count_uppers)
    print("строчных букв:", count_lowers)
    
txt = input("введите строку: ")
count(txt)