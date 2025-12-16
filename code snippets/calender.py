# calender print using the calender module
import datetime  #for getting the current tyme and date from the device
import calendar  #for printing the calender

today = datetime.date.today()   #creating the object for the datatime class

year = today.year  #for getting the current year
month = today.month #for getting the current month

print(calendar.month(year, month))  #for printing the calender 
