
# datetime module 

import datetime

                    # time(hour: int, minute: int, second: int, microsecond: int, tzinfo: tzinfo)
mytime = datetime.time(2, 20, 30, 15)

print(mytime)               # 02:20:30
print(mytime.hour)          # 2
print(mytime.minute)        # 20
print(mytime.second)        # 30
print(mytime.microsecond)   # 15
# print(mytime.tzinfo)
print(type(mytime))         # <class 'datetime.time'>    datetime object

                # date(year: int, month: int, day: int)
today_date = datetime.date.today()
print(today_date)            # 2020-12-05
print(today_date.year)       # 2020
print(today_date.month)      # 12
print(today_date.day)        # 05
print(type(today_date))      # <class 'datetime.date'>    datetime object   

# ctime()
print(today_date.ctime())   # Sat Dec  5 00:00:00 2020
# *************************************************************************************************


from datetime import datetime
my_datetime = datetime.now()
print(my_datetime)          # 2020-12-05 19:56:32.385542
print(datetime.now())       # 2020-12-05 19:56:32.385550
print(datetime.utcnow())    # 2020-12-06 03:56:32.385556
# print(datetime.tzinfo)     # <attribute 'tzinfo' of 'datetime.datetime' objects>

# *************************************************************************************************

from datetime import date 

day1 = date(2021, 11, 3)
day2 = date(2020, 11, 3)

result = day1 - day2
print(result)           # 365 days, 0:00:00
print(type(result))     # <class 'datetime.timedelta'>  timedelta object 
print(result.days)      # 365





