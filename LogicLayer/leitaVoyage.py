import csv
from LogicLayer.Date import*
from DataLayer.OpenFile import*
from ModelClasses.Voyage import*
from ModelClasses.flightRoute import*
from DataLayer.read_pastFlights import *

def leitaVoyage(inpt):

    #path = '/Users/hildur/Documents/github/verklegt_namskeid_1/Documents/github/Verklegt1/UPDATEDSTUDENTDATA/'
    #file1 = path + 'UpcomingFlights copy.csv'
    #file2 = path + 'PastFlights.csv'

    dest = inpt[2:4]
    no = int(inpt[4:len(inpt)])
    voyage = createVoyage()
    found_bool = 0

    if not found_bool:
        file1='UpcomingFlights copy3.csv'
    else:
        file1='PastFlights.csv'

    file_flights=OpenFile(file1)
    allPastFlights=read_pastFlights(file_flights)

    for j in range(len(allPastFlights)):

        deptTime = str(getDay(allPastFlights[j].departure)) + '/' + str(getMonth(allPastFlights[j].departure)) + '/' + str(getYear(allPastFlights[j].departure)) + ' at ' + str(getHour(allPastFlights[j].departure)) + ':' + str(getMinute(allPastFlights[j].departure))
        arvlTime = str(getDay(allPastFlights[j].arrival)) + '/' + str(getMonth(allPastFlights[j].arrival)) + '/' + str(getYear(allPastFlights[j].arrival)) + ' at ' + str(getHour(allPastFlights[j].arrival)) + ':' + str(getMinute(allPastFlights[j].arrival))

        if no%2 == 0 and allPastFlights[j].flightNumber == inpt:
            flight = createFlightRoute(allPastFlights[j].flightNumber, allPastFlights[j].departingFrom, allPastFlights[j].arrivingAt, deptTime, arvlTime,allPastFlights[j].aircraftId, allPastFlights[j].captain, allPastFlights[j].copilot, allPastFlights[j].fsm, allPastFlights[j].fa1, allPastFlights[j].fa2)
            voyage.departureFlight = flight
            #voyage.append(voy)

        elif no%2 == 0 and (allPastFlights[j].flightNumber == ('NA' + dest + str(no+1))):
            flight = createFlightRoute(allPastFlights[j].flightNumber, allPastFlights[j].departingFrom, allPastFlights[j].arrivingAt, deptTime, arvlTime,allPastFlights[j].aircraftId, allPastFlights[j].captain, allPastFlights[j].copilot, allPastFlights[j].fsm, allPastFlights[j].fa1, allPastFlights[j].fa2)
            voyage.returnFlight = flight
            #voyage.append(voy)

        elif no%2 != 0 and allPastFlights[j].flightNumber == inpt:
            flight = createFlightRoute(allPastFlights[j].flightNumber, allPastFlights[j].departingFrom, allPastFlights[j].arrivingAt, deptTime, arvlTime,allPastFlights[j].aircraftId, allPastFlights[j].captain, allPastFlights[j].copilot, allPastFlights[j].fsm, allPastFlights[j].fa1, allPastFlights[j].fa2)
            voyage.returnFlight = flight
            #voyage.append(voy)

        elif no%2 != 0 and allPastFlights[j].flightNumber == ('NA' + dest + str(no-1)):
            flight = createFlightRoute(allPastFlights[j].flightNumber, allPastFlights[j].departingFrom, allPastFlights[j].arrivingAt, deptTime, arvlTime,allPastFlights[j].aircraftId, allPastFlights[j].captain, allPastFlights[j].copilot, allPastFlights[j].fsm, allPastFlights[j].fa1, allPastFlights[j].fa2)
            voyage.departureFlight = flight
            #voyage.append(voy)

    return voyage
