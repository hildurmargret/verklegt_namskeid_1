import csv
from ModelClasses.flightRoute import*

def aircraftToVoyage(voyage):

    #fall sem vistar flugvél á vinnuferð í skrá
    
    voy=[]
    path="/Users/valdisbaerings/Documents/github/verklegt_namskeid_1/csvFiles/UpcomingFlights copy3.csv"
    departRoute=voyage.departureFlight
    retRoute=voyage.returnFlight

    with open(path,'r') as File1:
        csv_reader = csv.DictReader(File1)
        for row in csv_reader:
            v = createFlightRoute(row['flightNumber'],row['departingFrom'],row['arrivingAt'],row['departure'],row['arrival'],row['aircraftID'],row['soldTickets'],row['captain'],row['copilot'],row['fsm'],row['fa1'],row['fa2'])
            if v.flightNumber==departRoute.flightNumber and v.departure == departRoute.departure:
                voy.append(departRoute)
            elif v.flightNumber == retRoute.flightNumber and v.departure == retRoute.departure:
                voy.append(retRoute)
            else:
                voy.append(v)
    File1.close()
    return voy
