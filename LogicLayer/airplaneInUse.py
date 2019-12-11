from DataLayer.OpenFile import *
from DataLayer.read_pastFlights import *
from ModelClasses.flightRoute import *

def airplaneInUse(input_date, input_time, aircraftID):

    inptDay = str(input_date[0:2])
    inptMonth = str(input_date[3:5])
    inptYear = str(input_date[6:10])

    stdInptDate = inptYear + '-' + inptMonth + '-' + inptDay + 'T' + input_time

    if today>stdInptDate:
        file='PastFlights.csv'
    else:
        file='UpcomingFlights copy3.csv'

    file_flights=OpenFile(file)
    allFlights=read_pastFlights(file_flights)

    for i in range(len(allFlights)):
        if allFlights[i].
