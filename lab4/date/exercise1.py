from datetime import date, timedelta

current = date.today()

new_date = current - timedelta(days=5)

print("Current date: ", current)
print("Date after subtracting 5 days: ", new_date)
