from LogicLayer.Date import*
import csv
def saveUpdatedVoyage(voyage):
    voy=[]
    path="/Users/palinakroyer/github/verklegt_namskeid_1/csvFiles/UpcomingFlights copy.csv"
    departRoute=voyage.departureFlight
    retRoute=voyage.returnFlight
    date=getDay(retRoute.departure)

    with open(path,'r') as File1:
        csv_reader = csv.DictReader(File1)
        for row in csv_reader:
            v = createFlightRoute(row['flightNumber'],row['departingFrom'],row['arrivingAt'],row['departure'],row['arrival'],"",row['captain'],row['copilot'],row['fsm'],row['fa1'],row['fa2'])
            voy.append(v)
    File1.close()
    f=open(path, 'w')
    writer = csv.writer(f)
    writer.writerow( ('flightNumber','departingFrom','arrivingAt','departure','arrival','captain','copilot','fsm','fa1','fa2') )
    for i in range(len(voy)):
        if voy[i].flightNumber==departRoute.flightNumber:
            writer.writerow((departRoute.flightNumber,departRoute.departingFrom,departRoute.arrivingAt,departRoute.departure,departRoute.arrival,departRoute.captain,departRoute.copilot,departRoute.fsm,departRoute.fa1,departRoute.fa2))
        elif voy[i-1].flightNumber==(departRoute.flightNumber):
            writer.writerow((retRoute.flightNumber,retRoute.departingFrom,retRoute.arrivingAt,retRoute.departure,retRoute.arrival,retRoute.captain,retRoute.copilot,retRoute.fsm,retRoute.fa1,retRoute.fa2))
        else:
            writer.writerow((voy[i].flightNumber,voy[i].departingFrom,voy[i].arrivingAt,voy[i].departure,voy[i].arrival,voy[i].captain,voy[i].copilot,voy[i].fsm,voy[i].fa1,voy[i].fa2))
    f.close()
