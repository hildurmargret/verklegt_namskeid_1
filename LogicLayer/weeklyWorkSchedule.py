from LogicLayer.Date import*
from LogicLayer.getStaff5_6 import*
def weeklyWS(week,year,input_string):

    flights = []
    retFlights = []

    dateRange = getDateRangeFromWeek(week, year)

    firstDay = str(getDay(dateRange[1]))
    firstMonth = str(getMonth(dateRange[1]))
    firstYear = str(getYear(dateRange[1]))

    lastDay = str(getDay(dateRange[0]))
    lastMonth = str(getMonth(dateRange[0]))
    lastYear = str(getYear(dateRange[0]))

    numOfDest, pastFlights, upcFlights, employees = staffInfo2(input_string)

    today=now()

    if today>dateRange[1]:
        flights = pastFlights
    else:
        flights = pastFlights

    for i in range(len(flights)):
        day = str(flights[i].departure[0:2])
        month = str(flights[i].departure[3:5])
        year = str(flights[i].departure[6:10])
        stdTime = year + '-' + month + '-' + day + 'T00:00:00'

        if stdTime >= dateRange[1] and stdTime <= dateRange[0]:
            retFlights.append(flights[i])


    return retFlights, employees
