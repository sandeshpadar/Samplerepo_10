# datedifference

from datetime import datetime, timedelta
current_date = datetime.today()
print(current_date)

new = current_date - timedelta(days = 2)
print(new)
