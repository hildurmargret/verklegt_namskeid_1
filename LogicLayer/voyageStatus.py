from DataLayer.OpenFile import *
from DataLayer.read_pastFlights import *
from ModelClasses.flightRoute import *
from LogicLayer.Date import *
from ModelClasses.Voyage import*

def voyageStatus(dep, ret, input_date, input_time):

    inptDay = str(input_date[0:2])
    inptMonth = str(input_date[3:5])
    inptYear = str(input_date[6:10])

    stdInptDate = inptYear + '-' + inptMonth + '-' + inptDay + 'T' + input_time
    timabil=add_hour(stdInptDate, (-2))

    status=[]

    #print(len(ret))
    #print(len(dep))

    for i in range(len(dep)):
        if timabil < dep[i].departure <= stdInptDate:
            status.append('In air outbound')
        elif timabil < ret[i].departure <= stdInptDate:
            status.append('In air homebound')
        elif timabil > dep[i].departure:
            status.append('On ground at home')
        elif timabil > ret[i].departure:
            status.append('On ground at destination')
        elif ret[i].departure > stdInptDate:
            status.append('Completed')


    return status

    # inptDay = str(input_date[0:2])
    # inptMonth = str(input_date[3:5])
    # inptYear = str(input_date[6:10])
    #
    # stdInptDate = inptYear + '-' + inptMonth + '-' + inptDay + 'T' + input_time
    #
    # today=now()
    #
    # if today>stdInptDate:
    #     file='PastFlights copy.csv'
    # else:
    #     file='UpcomingFlights copy3.csv'
    #
    # file_flights=OpenFile(file)
    # allFlights=read_pastFlights(file_flights)
    #
    # timabil=add_hour(stdInptDate, (-2))
    # print(stdInptDate)
    # print(timabil)
    #
    # status=[]
    # voyages=[]
    #
    # for i in range(len(allFlights)):
    #     print(str(getDay(allFlights[i].departure)))
    #     if inptDay == str(getDay(allFlights[i].departure)) and inptMonth == str(getMonth(allFlights[i].departure)) and inptYear == str(getYear(allFlights[i].departure)):
    #         if timabil < allFlights[i].departure and allFlights[i].departure <= stdInptDate and allFlights[i].arrivingAt == 'KEF':
    #             #print(allFlights[i].flightNumber)
    #             status.append('In air homebound')
    #
    #         elif timabil < allFlights[i].departure and allFlights[i].departure <= stdInptDate and allFlights[i].arrivingAt != 'KEF':
    #             status.append('In air outbound')
    #
    #         elif timabil > allFlights[i].departure:
    #             status.append('Not begun')
    #
    #         elif allFlights[i].departure > stdInptDate:
    #             status.append('Completed')
    #
    #         print(int(allFlights[i].flightNumber[2:len(allFlights[i].flightNumber)])%2)
    #
    #         print(int(allFlights[i].flightNumber[2:len(allFlights[i].flightNumber)]))
    #
    #         if int(allFlights[i].flightNumber[2:len(allFlights[i].flightNumber)])%2 == 0:
    #             voyage = createVoyage()
    #
    #             depFlight = createFlightRoute(allFlights[i].flightNumber, allFlights[i].departingFrom, allFlights[i].arrivingAt,allFlights[i].departure,allFlights[i].arrival,allFlights[i].aircraftId, allFlights[i].captain, allFlights[i].copilot, allFlights[i].fsm, allFlights[i].fa1, allFlights[i].fa2)
    #             voyage.departureFlight = depFlight
    #             retFlight = createFlightRoute(allFlights[i+1].flightNumber, allFlights[i+1].departingFrom, allFlights[i+1].arrivingAt,allFlights[i+1].departure,allFlights[i+1].arrival,allFlights[i+1].aircraftId, allFlights[i+1].captain, allFlights[i+1].copilot, allFlights[i+1].fsm, allFlights[i+1].fa1, allFlights[i+1].fa2)
    #             voyage.returnFlight = retFlight
    #             voyages.append(voyage)
    #         else:
    #             voyage = createVoyage()
    #
    #             depFlight = createFlightRoute(allFlights[i-1].flightNumber, allFlights[i-1].departingFrom, allFlights[i-1].arrivingAt,allFlights[i-1].departure,allFlights[i-1].arrival,allFlights[i-1].aircraftId, allFlights[i-1].captain, allFlights[i-1].copilot, allFlights[i-1].fsm, allFlights[i-1].fa1, allFlights[i-1].fa2)
    #             voyage.departureFlight = depFlight
    #             retFlight = createFlightRoute(allFlights[i].flightNumber, allFlights[i].departingFrom, allFlights[i].arrivingAt,allFlights[i].departure,allFlights[i].arrival,allFlights[i].aircraftId, allFlights[i].captain, allFlights[i].copilot, allFlights[i].fsm, allFlights[i].fa1, allFlights[i].fa2)
    #             voyage.returnFlight = retFlight
    #             voyages.append(voyage)
    #
    # return voyages, status
