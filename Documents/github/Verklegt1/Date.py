import datetime
import dateutil.parser
from time import strftime,gmtime
#import string

def getDate(year,month,day,hour,minute):
    date=datetime.datetime(year,month,day,hour,minute,0).isoformat()
    return date

def getYear(date):
    parsedDate = dateutil.parser.parse(date)
    return parsedDate.year

def getMonth(date):
    parsedDate = dateutil.parser.parse(date)
    return parsedDate.month

def getDay(date):
    parsedDate = dateutil.parser.parse(date)
    return parsedDate.day

def getHour(date):
    parsedDate = dateutil.parser.parse(date)
    return parsedDate.hour

def getMinute(date):
    parsedDate = dateutil.parser.parse(date)
    return parsedDate.minute

def getSecond(date):
    parsedDate = dateutil.parser.parse(date)
    return parsedDate.second


def time_now():
    now=datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current time = ", current_time )

date=getDate(2020,11,23,11,43)
year=getYear(date)
month=getMonth(date)
day=getDay(date)
hour=getHour(date)
minute=getMinute(date)
second=getSecond(date)

#print(year)
#print(month)
#print(day)
#print(hour)
#print(minute)
#print(second)
