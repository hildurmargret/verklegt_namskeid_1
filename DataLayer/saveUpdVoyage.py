from DataLayer.read_pastFlights import*
from LogicLayer.Date import*
import csv
import sys
import os
def saveUpdVoyage(voyage):

    today=now()

    if today>voyage.departureFlight.departure:
        file='PastFlights copy.csv'
    else:
        file='UpcomingFlights copy3.csv'

    flights = read_pastFlights(file)
    newFlights = []

    for flight in flights:
        if flight.flightNumber == voyage.departureFlight.flightNumber and flight.departure == voyage.departureFlight.departure:
            newFlight = createFlightRoute(voyage.departureFlight.flightNumber, voyage.departureFlight.departingFrom, voyage.departureFlight.arrivingAt,voyage.departureFlight.departure, voyage.departureFlight.arrival,voyage.departureFlight.aircraftId,voyage.departureFlight.soldTickets,voyage.departureFlight.captain,voyage.departureFlight.copilot,voyage.departureFlight.fsm,voyage.departureFlight.fa1,voyage.departureFlight.fa2)
            newFlights.append(newFlight)
        elif flight.flightNumber == voyage.returnFlight.flightNumber and flight.departure == voyage.returnFlight.departure:
            newFlight = createFlightRoute(voyage.returnFlight.flightNumber, voyage.returnFlight.departingFrom, voyage.returnFlight.arrivingAt,voyage.returnFlight.departure, voyage.returnFlight.arrival,voyage.returnFlight.aircraftId,voyage.returnFlight.soldTickets,voyage.returnFlight.captain,voyage.returnFlight.copilot,voyage.returnFlight.fsm,voyage.returnFlight.fa1,voyage.returnFlight.fa2)
            newFlights.append(newFlight)
        else:
            newFlights.append(flight)

    absPathFile = os.path.abspath(__file__)
    fileDir = os.path.dirname(os.path.abspath(__file__))
    parentDir = os.path.dirname(fileDir)
    path = parentDir + "/csvFiles/" + file

    f=open(path, 'w')
    writer = csv.writer(f)
    writer.writerow( ('flightNumber','departingFrom','arrivingAt','departure','arrival','aircraftID','soldTickets','captain','copilot','fsm','fa1','fa2') )

    for flight in newFlights:
        writer.writerow((flight.flightNumber,flight.departingFrom,flight.arrivingAt,flight.departure,flight.arrival,flight.aircraftId,flight.soldTickets,flight.captain,flight.copilot,flight.fsm,flight.fa1,flight.fa2))
