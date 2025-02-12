#1
from datetime import datetime, timedelta

c = datetime.today()
n = c - timedelta(days=5)
print("Date five days ago:", n.strftime("%d.%m.%Y"))
#2
from datetime import datetime, timedelta

t = datetime.today()
y = t - timedelta(days=1)
to = t + timedelta(days=1)

print("Yesterday:", y.strftime("%d.%m.%Y"))
print("Today:", t.strftime("%d.%m.%Y"))
print("Tomorrow:", to.strftime("%d.%m.%Y"))

#3
from datetime import datetime

n = datetime.now()
w = n.replace(microsecond=0)
print("Current time without microseconds:", w)

#4
from datetime import datetime

d1 = datetime(2025, 2, 10, 12, 0, 0)  # Example date 1
d2 = datetime(2025, 2, 12, 15, 30, 0)  # Example date 2

d = abs((d2 - d1).total_seconds())
print("Difference in seconds:", d)
