import csv
from LogicLayer.Date import*
from DataLayer.OpenFile import*
from ModelClasses.Voyage import*
from ModelClasses.flightRoute import*
from DataLayer.read_pastFlights import *
from UILayer.chooseVoyageFromList import*

def leitaVoyage(inpt):

    dest = inpt[2:4]
    no = int(inpt[4:len(inpt)])
    voyages =[]
    found_bool = 0

    #if not found_bool:
    #    file1='UpcomingFlights copy3.csv'
    #else:
    file1='PastFlights copy.csv'

    file_flights=OpenFile(file1)
    allPastFlights=read_pastFlights(file_flights)

    for j in range(len(allPastFlights)):

        if no%2 == 0 and allPastFlights[j].flightNumber == inpt:
            voyage = createVoyage()
            depDeptTime = str(getDay(allPastFlights[j].departure)) + '/' + str(getMonth(allPastFlights[j].departure)) + '/' + str(getYear(allPastFlights[j].departure)) + ' at ' + str(getHour(allPastFlights[j].departure)) + ':' + str(getMinute(allPastFlights[j].departure))
            depArvlTime = str(getDay(allPastFlights[j].arrival)) + '/' + str(getMonth(allPastFlights[j].arrival)) + '/' + str(getYear(allPastFlights[j].arrival)) + ' at ' + str(getHour(allPastFlights[j].arrival)) + ':' + str(getMinute(allPastFlights[j].arrival))
            arrDeptTime = str(getDay(allPastFlights[j+1].departure)) + '/' + str(getMonth(allPastFlights[j+1].departure)) + '/' + str(getYear(allPastFlights[j+1].departure)) + ' at ' + str(getHour(allPastFlights[j+1].departure)) + ':' + str(getMinute(allPastFlights[j+1].departure))
            arrArvlTime = str(getDay(allPastFlights[j+1].arrival)) + '/' + str(getMonth(allPastFlights[j+1].arrival)) + '/' + str(getYear(allPastFlights[j+1].arrival)) + ' at ' + str(getHour(allPastFlights[j+1].arrival)) + ':' + str(getMinute(allPastFlights[j+1].arrival))

            depFlight = createFlightRoute(allPastFlights[j].flightNumber, allPastFlights[j].departingFrom, allPastFlights[j].arrivingAt, depDeptTime, depArvlTime,allPastFlights[j].aircraftId, allPastFlights[j].captain, allPastFlights[j].copilot, allPastFlights[j].fsm, allPastFlights[j].fa1, allPastFlights[j].fa2)
            voyage.departureFlight = depFlight
            retFlight = createFlightRoute(allPastFlights[j+1].flightNumber, allPastFlights[j+1].departingFrom, allPastFlights[j+1].arrivingAt, arrDeptTime, arrArvlTime,allPastFlights[j+1].aircraftId, allPastFlights[j+1].captain, allPastFlights[j+1].copilot, allPastFlights[j+1].fsm, allPastFlights[j+1].fa1, allPastFlights[j+1].fa2)
            voyage.returnFlight = retFlight
            voyages.append(voyage)


        elif no%2 != 0 and allPastFlights[j].flightNumber == inpt:
            voyage = createVoyage()
            arrDeptTime = str(getDay(allPastFlights[j].departure)) + '/' + str(getMonth(allPastFlights[j].departure)) + '/' + str(getYear(allPastFlights[j].departure)) + ' at ' + str(getHour(allPastFlights[j].departure)) + ':' + str(getMinute(allPastFlights[j].departure))
            arrArvlTime = str(getDay(allPastFlights[j].arrival)) + '/' + str(getMonth(allPastFlights[j].arrival)) + '/' + str(getYear(allPastFlights[j].arrival)) + ' at ' + str(getHour(allPastFlights[j].arrival)) + ':' + str(getMinute(allPastFlights[j].arrival))
            depDeptTime = str(getDay(allPastFlights[j-1].departure)) + '/' + str(getMonth(allPastFlights[j-1].departure)) + '/' + str(getYear(allPastFlights[j-1].departure)) + ' at ' + str(getHour(allPastFlights[j-1].departure)) + ':' + str(getMinute(allPastFlights[j-1].departure))
            depArvlTime = str(getDay(allPastFlights[j-1].arrival)) + '/' + str(getMonth(allPastFlights[j-1].arrival)) + '/' + str(getYear(allPastFlights[j-1].arrival)) + ' at ' + str(getHour(allPastFlights[j-1].arrival)) + ':' + str(getMinute(allPastFlights[j-1].arrival))

            depFlight = createFlightRoute(allPastFlights[j-1].flightNumber, allPastFlights[j-1].departingFrom, allPastFlights[j-1].arrivingAt, depDeptTime, depArvlTime,allPastFlights[j-1].aircraftId, allPastFlights[j-1].captain, allPastFlights[j-1].copilot, allPastFlights[j-1].fsm, allPastFlights[j-1].fa1, allPastFlights[j-1].fa2)
            voyage.departureFlight = depFlight
            retFlight = createFlightRoute(allPastFlights[j].flightNumber, allPastFlights[j].departingFrom, allPastFlights[j].arrivingAt, arrDeptTime, arrArvlTime,allPastFlights[j].aircraftId, allPastFlights[j].captain, allPastFlights[j].copilot, allPastFlights[j].fsm, allPastFlights[j].fa1, allPastFlights[j].fa2)
            voyage.returnFlight = retFlight
            voyages.append(voyage)

    retVoyage = chooseVoyage(voyages)

    return retVoyage
