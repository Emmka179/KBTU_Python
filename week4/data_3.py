import datetime

x = datetime.datetime.now().replace(microsecond=0)
y = x - datetime.timedelta(days=5)
print(f'Date: {x}')
print(f'Date: {y}')