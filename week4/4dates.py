from datetime import datetime
year1, month1, day1, hour1, minute1, second1 = map(int, input("первая дата: ").split())
year2, month2, day2, hour2, minute2, second2= map(int, input("вторая дата: ").split())

date1 = datetime(year1, month1, day1, hour1, minute1, second1)
date2 = datetime(year2, month2, day2, hour2, minute2, second2) 

dif = abs(date2 - date1).total_seconds()
print("разница в секундах:", dif)