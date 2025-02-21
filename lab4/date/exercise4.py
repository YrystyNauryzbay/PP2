from datetime import datetime

date1 = datetime.now()
date2 = datetime.now()

difference = date2 - date1

difference_in_seconds = difference.total_seconds()

print(date1, "and", date2)
print("Difference in seconds:", difference_in_seconds)
