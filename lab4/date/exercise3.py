from datetime import datetime

current_datetime = datetime.now()


without_microseconds = current_datetime.replace(microsecond=0)

print("Current datetime with microseconds:", current_datetime)
print("Datetime without microseconds:", without_microseconds)
