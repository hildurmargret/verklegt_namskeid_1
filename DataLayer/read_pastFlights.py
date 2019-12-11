import csv
from ModelClasses.flightRoute import *

def read_pastFlights(file_name):

    pastFlights=[]

    with file_name as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            flight = createFlightRoute(row['flightNumber'], row['departingFrom'], row['arrivingAt'], row['departure'], row['arrival'], row['aircraftID'], row['captain'], row['copilot'], row['fsm'], row['fa1'], row['fa2'])
            pastFlights.append(flight)

    return pastFlights
