from LogicLayer.Date import*
import csv
from ModelClasses.flightRoute import*
from DataLayer.read_pastFlights import*

def saveUpdatedVoyage(voyage):

    voy=[]

    path="/Users/valdisbaerings/Documents/github/verklegt_namskeid_1/csvFiles/UpcomingFlights copy3.csv"
    #by til voyage klasatilvik
    departRoute=voyage.departureFlight
    retRoute=voyage.returnFlight

    #tek oll voyage ut skranni og bæti við nyju
    with open(path,'r') as File1:
        csv_reader = csv.DictReader(File1)

        for row in csv_reader:
            v = createFlightRoute(row['flightNumber'],row['departingFrom'],row['arrivingAt'],row['departure'],row['arrival'],row['aircraftID'],row['soldTickets'],row['captain'],row['copilot'],row['fsm'],row['fa1'],row['fa2'])
            voy.append(v)
        #her bæti við
        voy.append(departRoute)
        voy.append(retRoute)

    return voy
