import csv
from ModelClasses.Voyage import*
def airportOccupied(newVoyage):
    depFlight=newVoyage.departureFlight
    retFlight=newVoyage.returnFlight
    boolAirportOccupied=False
    path="/Users/valdisbaerings/Documents/github/verklegt_namskeid_1/csvFiles/UpcomingFlights copy3.csv"
    voy=[]
    newDate=retFlight.departure

    with open(path,'r') as File1:
        csv_reader = csv.DictReader(File1)
        for row in csv_reader:
            v = createFlightRoute(row['flightNumber'],row['departingFrom'],row['arrivingAt'],row['departure'],row['arrival'],row['aircraftID'],row['soldTickets'],row['captain'],row['copilot'],row['fsm'],row['fa1'],row['fa2'])
            voy.append(v)
            oldDate=v.departure

            if newDate==oldDate:
                print("The airport is already occupied")
                boolAirportOccupied=True
    File1.close()
    if boolAirportOccupied==False:
        voy.append(depFlight)
        voy.append(retFlight)
    return voy
