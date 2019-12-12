import csv
from ModelClasses.flightRoute import*

def aircraftToVoyage(voyage):
    voy=[]
    path="/Users/palinakroyer/github/verklegt_namskeid_1/csvFiles/UpcomingFlights copy.csv"
    departRoute=voyage.departureFlight
    retRoute=voyage.returnFlight
    # print("HIII")
    # print(departRoute.aircraftId)
    # print(type(departRoute))
    # print(retRoute)
    # print(type(retRoute))

    with open(path,'r') as File1:
        csv_reader = csv.DictReader(File1)
        for row in csv_reader:
            v = createFlightRoute(row['flightNumber'],row['departingFrom'],row['arrivingAt'],row['departure'],row['arrival'],row['aircraftID'],row['soldTickets'],row['captain'],row['copilot'],row['fsm'],row['fa1'],row['fa2'])
            voy.append(v)
            if v.flightNumber==departRoute.flightNumber:
                voy.append(v)
            elif v.flightNumber==departRoute.flightNumber:
                voy.append(v)
    File1.close()
    return voy
