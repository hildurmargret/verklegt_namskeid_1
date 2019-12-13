from LogicLayer.Date import*
import csv
from ModelClasses.flightRoute import*
from LogicLayer.Date import*
from DataLayer.read_pastFlights import*
def saveUpVoy(voyage):
    voy=[]

    departRoute=voyage.departureFlight
    retRoute=voyage.returnFlight

    today=now()
    if today>departRoute.departure:
        path="/Users/valdisbaerings/Documents/github/verklegt_namskeid_1/csvFiles/PastFlights copy.csv"
    else:
        path="/Users/valdisbaerings/Documents/github/verklegt_namskeid_1/csvFiles/UpcomingFlights copy3.csv"

    with open(path,'r') as File1:
        csv_reader = csv.DictReader(File1)
        #print(departRoute.flightNumber)
        for row in csv_reader:
            v = createFlightRoute(row['flightNumber'],row['departingFrom'],row['arrivingAt'],row['departure'],row['arrival'],row['aircraftID'],row['soldTickets'],row['captain'],row['copilot'],row['fsm'],row['fa1'],row['fa2'])
            voy.append(v)

        #voy.append(departRoute)
        #voy.append(retRoute)


    File1.close()
    f=open(path, 'w')
    writer = csv.writer(f)
    writer.writerow( ('flightNumber','departingFrom','arrivingAt','departure','arrival','aircraftID','soldTickets','captain','copilot','fsm','fa1','fa2') )
    for i in range(len(voy)):
        if voy[i].flightNumber==departRoute.flightNumber and voy[i].departure==departRoute.departure:
            writer.writerow((departRoute.flightNumber,departRoute.departingFrom,departRoute.arrivingAt,departRoute.departure,departRoute.arrival,departRoute.aircraftId,departRoute.soldTickets,departRoute.captain,departRoute.copilot,departRoute.fsm,departRoute.fa1,departRoute.fa2))
        elif voy[i-1].flightNumber==departRoute.flightNumber and voy[i-1].departure==departRoute.departure:
            writer.writerow((retRoute.flightNumber,retRoute.departingFrom,retRoute.arrivingAt,retRoute.departure,retRoute.arrival,retRoute.aircraftId,retRoute.soldTickets,retRoute.captain,retRoute.copilot,retRoute.fsm,retRoute.fa1,retRoute.fa2))
        else:
            writer.writerow((voy[i].flightNumber,voy[i].departingFrom,voy[i].arrivingAt,voy[i].departure,voy[i].arrival,voy[i].aircraftId,voy[i].soldTickets,voy[i].captain,voy[i].copilot,voy[i].fsm,voy[i].fa1,voy[i].fa2))
    f.close()
    #print("\n")
    #print(len(voy))
    return voy
