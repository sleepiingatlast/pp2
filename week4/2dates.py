from datetime import datetime, timedelta

today = datetime.today()
yesterday = today - timedelta(days = 1)
tomorrow = today + timedelta(days = 1)

print("yesterday was:", yesterday.strftime("%d"), yesterday.strftime("%B"))
print("today is:", today.strftime("%d"), today.strftime("%B"))
print("tomorrow will be:", tomorrow.strftime("%d"), tomorrow.strftime("%B"))