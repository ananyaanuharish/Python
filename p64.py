import os 
os .system('cls')

# to display month
import calendar
yy = 2025
mm = 2
print(calendar.month(yy, mm))

# to display whole year
yy = 2022
print(calendar.calendar(yy))

# to display current date and time
import datetime
current_time = datetime.datetime.now()
print("time is:",current_time)