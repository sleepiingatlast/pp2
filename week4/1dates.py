from datetime import datetime, timedelta

now = datetime.today()
another = now - timedelta(days = 5)

print("5 days before today was:", another.strftime("%d"), another.strftime("%B"))