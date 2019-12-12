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
    done_bool = 0

    #if not found_bool:
    #    file1='UpcomingFlights copy3.csv'
    #else:
    file1='PastFlights copy.csv'
    while not done_bool:
        if file1 == 'UpcomingFlights copy3.csv':
            done_bool=1
        file_flights=OpenFile(file1)
        allPastFlights=read_pastFlights(file_flights)

        for j in range(len(allPastFlights)):

            if no%2 == 0 and allPastFlights[j].flightNumber == inpt:
                voyage = createVoyage()

                depFlight = createFlightRoute(allPastFlights[j].flightNumber, allPastFlights[j].departingFrom, allPastFlights[j].arrivingAt,allPastFlights[j].departure,allPastFlights[j].arrival,allPastFlights[j].aircraftId, allPastFlights[j].captain, allPastFlights[j].copilot, allPastFlights[j].fsm, allPastFlights[j].fa1, allPastFlights[j].fa2)
                voyage.departureFlight = depFlight
                retFlight = createFlightRoute(allPastFlights[j+1].flightNumber, allPastFlights[j+1].departingFrom, allPastFlights[j+1].arrivingAt,allPastFlights[j+1].departure,allPastFlights[j+1].arrival,allPastFlights[j+1].aircraftId, allPastFlights[j+1].captain, allPastFlights[j+1].copilot, allPastFlights[j+1].fsm, allPastFlights[j+1].fa1, allPastFlights[j+1].fa2)
                voyage.returnFlight = retFlight
                voyages.append(voyage)


            elif no%2 != 0 and allPastFlights[j].flightNumber == inpt:
                voyage = createVoyage()

                depFlight = createFlightRoute(allPastFlights[j-1].flightNumber, allPastFlights[j-1].departingFrom, allPastFlights[j-1].arrivingAt,allPastFlights[j-1].departure,allPastFlights[j-1].arrival,allPastFlights[j-1].aircraftId, allPastFlights[j-1].soldTickets,allPastFlights[j-1].captain, allPastFlights[j-1].copilot, allPastFlights[j-1].fsm, allPastFlights[j-1].fa1, allPastFlights[j-1].fa2)
                voyage.departureFlight = depFlight
                retFlight = createFlightRoute(allPastFlights[j].flightNumber, allPastFlights[j].departingFrom, allPastFlights[j].arrivingAt,allPastFlights[j].departure,allPastFlights[j].arrival,allPastFlights[j].aircraftId,allPastFlights[j].soldTickets, allPastFlights[j].captain, allPastFlights[j].copilot, allPastFlights[j].fsm, allPastFlights[j].fa1, allPastFlights[j].fa2)
                voyage.returnFlight = retFlight
                voyages.append(voyage)
        file1 = 'UpcomingFlights copy3.csv'

    #retVoyage = chooseVoyage(voyages)

    return voyages #retVoyage
