import datetime
import dateutil.parser
import time
#from time import strftime,gmtime
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

def getWeekNumber(year, month, date):
    WeekNumber = datetime.date(year, month, date).strftime("%V")
    return WeekNumber


def getDateRangeFromWeek(week_number, year_int):
    weekdates = []
    year = str(year_int)
    for day in range(7):
        week_date = datetime.datetime.strptime(year+"-W{}".format(week_number)+ '-{}'.format(day), "%Y-W%W-%w").isoformat()
        weekdates.append(week_date)
    return weekdates


def time_now():
    now=datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time
    #print("Current time = ", current_time )

def date_now():
    today = datetime.datetime.today()
    d1 = today.strftime("%Y-%m-%d""T""%H:%M:%S")
    return d1



#getDateRangeFromWeek(23, 2019)

#getDateRangeFromWeek(2019,44)
