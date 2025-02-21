from datetime import date, timedelta

current = date.today()

yesterday = current - timedelta(days=1)

tomorrow = current + timedelta(days=1)

print(current)
print(yesterday, tomorrow)