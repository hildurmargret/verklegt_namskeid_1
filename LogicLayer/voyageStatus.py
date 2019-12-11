from DataLayer.OpenFile import *
from DataLayer.read_pastFlights import *
from ModelClasses.flightRoute import *
from LogicLayer.Date import *

def voyageStatus(input_date, input_time):

    inptDay = str(input_date[0:2])
    inptMonth = str(input_date[3:5])
    inptYear = str(input_date[6:10])

    stdInptDate = inptYear + '-' + inptMonth + '-' + inptDay + 'T' + input_time

    today=now()

    if today>stdInptDate:
        file='PastFlights.csv'
    else:
        file='UpcomingFlights copy3.csv'

    file_flights=OpenFile(file)
    allFlights=read_pastFlights(file_flights)

    timabil=add_hour(stdInptDate, (-2))

    status=[]

    for i in range(len(allFlights)):
        if inptDay == str(getDay(allFlights[i].departure)) and inptMonth == str(getMonth(allFlights[i].departure)) and inptYear == str(getYear(allFlights[i].departure)):

            if timabil < allFlights[i].departure and allFlights[i].departure <= stdInptDate and allFlights[i].arrivingAt == 'KEF':
                status[i]='In air homebound'

            elif timabil < allFlights[i].departure and allFlights[i].departure <= stdInptDate and allFlights[i].arrivingAt != 'KEF':
                status[i]='In air outbound'

            elif timabil > allFlights[i].departure:
                status[i]='Not begun'

            elif allFlights[i].departure > stdInptDate:
                status[i]='Completed'

            flights=createFlightRoute(allFlights[i].flightNumber, allFlights[i].departingFrom,allFlights[i].arrivingAt, allFlights[i].departure, allFlights[i].arrival, allFlights[i].aircraftId, allFlights[i].captain, allFlights[i].copilot, allFlights[i].fsm, allFlights[i].fa1, allFlights[i].fa2)

    return flights, status
