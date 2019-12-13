from LogicLayer.Date import*
import csv
from ModelClasses.flightRoute import*
from LogicLayer.Date import*
from DataLayer.read_pastFlights import*
import sys
import os
from DataLayer.OpenFile import*
def saveUpVoy(voyage):
    voy=[]

    departRoute=voyage.departureFlight
    retRoute=voyage.returnFlight
    #finn viðeigandi skra
    today=now()
    if today>departRoute.departure:
        file="PastFlights copy.csv"
    else:
        file="UpcomingFlights copy3.csv"

    path = OpenFile(file)

    #opna og les uppur i lista
    with path as File1:
        csv_reader = csv.DictReader(File1)
        for row in csv_reader:
            v = createFlightRoute(row['flightNumber'],row['departingFrom'],row['arrivingAt'],row['departure'],row['arrival'],row['aircraftID'],row['soldTickets'],row['captain'],row['copilot'],row['fsm'],row['fa1'],row['fa2'])
            voy.append(v)

    absPathFile = os.path.abspath(__file__)
    fileDir = os.path.dirname(os.path.abspath(__file__))
    parentDir = os.path.dirname(fileDir)
    path = parentDir + "/csvFiles/" + file

    #bæti inni skra soldTickets
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

    return voy
