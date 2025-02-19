import datetime

x = datetime.datetime.now()
y = x - datetime.timedelta(days=5)
print(x.strftime('%x'))
print(y.strftime('%x'))