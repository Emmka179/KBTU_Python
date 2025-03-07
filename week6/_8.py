import os

path = input()

if not os.path.exists(path):
    print('Path does not exists')
    exit()

if os.access(path, os.R_OK):
    print('Path is ok to Read')
    os.remove(path)
else: print('Path os not ok to Read')

if os.access(path, os.W_OK):
    print('Path is ok to Write')
    os.remove(path)
else: print('Path is not ok to Write')

if os.access(path, os.EX_OK):
    print('Path is ok to Execute')
    os.remove(path)
else: print('Path is not ok to Exectute')