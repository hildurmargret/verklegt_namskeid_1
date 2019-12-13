import csv
from DataLayer.OpenFile import*
from ModelClasses.flightRoute import *

def read_pastFlights(file):

    #fall sem nær í öll flug úr skrá og býr til klasatilvikalista af þeim
    pastFlights=[]

    file_name=OpenFile(file)

    with file_name as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            flight = createFlightRoute(row['flightNumber'], row['departingFrom'], row['arrivingAt'], row['departure'], row['arrival'], row['aircraftID'], row['soldTickets'], row['captain'], row['copilot'], row['fsm'], row['fa1'], row['fa2'])
            pastFlights.append(flight)

    return pastFlights
