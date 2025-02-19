import datetime

x = datetime.datetime.now()
y = x - datetime.timedelta(days=8)

difference = (x - y).total_seconds()
print(x.strftime('%x'))
print(y.strftime('%x'))
print(f"Difference in seconds: {difference}")