import datetime

date = str(datetime.datetime.now())
date = date.split()[0].split('-')
year = int(date[0])
month = int(date[1])
day = int(date[2])
print(2025 == year)