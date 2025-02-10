# import datetime
# print(dir(datetime))

from datetime import datetime
import pytz
now = datetime.now()  # method1 # give current date and time
now=datetime(2026,10,1) # method2 # give the date an time we give
now.strftime("%m/%d/%Y")  #chan
newvar=datetime.now(pytz.timezone('Asia/kolkata'))
day = now.day
month = now.month
year = now.year
minute = now.minute
second = now.second

print("Current date and time: ",now)
print(f'Day={day}/Month={month}/Year={year}/minute={minute}/second={second}')
print(newvar)