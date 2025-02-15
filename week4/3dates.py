from datetime import datetime, timedelta

current = datetime.now()
without_micros = current.replace(microsecond = 0)

print("было:", current)
print("стало:", without_micros)