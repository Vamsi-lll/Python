# calender print using the calender module
import datetime
import calendar

today = datetime.date.today()

year = today.year
month = today.month

print(calendar.month(year, month))
