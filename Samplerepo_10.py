# datedifference

from datetime import datetime, timedelta
current_date = datetime.today()
print(current_date)

new = current_date - timedelta(days = 2)
print(new)

import datetime
current_date = datetime.datetime.now()
print(current_date)
print(current_date.year)
print(current_date.month)
print(current_date.day)
print(current_date.hour)
print(current_date.minute)
print(current_date.second)
print(current_date.microsecond)
print(current_date.strftime('%A'))
print(current_date.strftime('%B'))
print(current_date.strftime('%a'))
print(current_date.strftime('%b'))
