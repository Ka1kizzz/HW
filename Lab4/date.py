#ex1
from datetime import datetime, timedelta

current_date = datetime.now()
five_days_ago = current_date - timedelta(days=5)

print("Дата:", current_date)
print(":", five_days_ago)

#ex2
from datetime import datetime, timedelta

today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

#ex3
from datetime import datetime

current_datetime = datetime.now()
current_datetime_without_microseconds = current_datetime.replace(microsecond=0)

print("Current Datetime:", current_datetime)
print("Current Datetime without Microseconds:", current_datetime_without_microseconds)

#ex4
from datetime import datetime

current_datetime = datetime.now()
current_datetime_without_microseconds = current_datetime.replace(microsecond=0)

print("Current Datetime:", current_datetime)
print("Current Datetime without Microseconds:", current_datetime_without_microseconds)
