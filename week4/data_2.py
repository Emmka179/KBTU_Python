import datetime
today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)
print(f'Today: {today.strftime("%x")}')
print(f'Yesterday: {yesterday.strftime("%x")}')
print(f'Tomorrow: {tomorrow.strftime("%x")}')