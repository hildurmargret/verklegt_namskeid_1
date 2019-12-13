import csv
from DataLayer.OpenFile import*
from ModelClasses.Voyage import*
def airportOccupied(newVoyage):
    depFlight=newVoyage.departureFlight
    retFlight=newVoyage.returnFlight
    boolAirportOccupied=False
    ##path="/Users/valdisbaerings/Documents/github/verklegt_namskeid_1/csvFiles/UpcomingFlights copy3.csv"
    voy=[]
    newDateDep=newVoyage.departureFlight.departure
    newDateRet=newVoyage.returnFlight.arrival

    file = OpenFile('UpcomingFlights copy3.csv')

    with file as File1:
        csv_reader = csv.DictReader(File1)
        for row in csv_reader:
            v = createFlightRoute(row['flightNumber'],row['departingFrom'],row['arrivingAt'],row['departure'],row['arrival'],row['aircraftID'],row['soldTickets'],row['captain'],row['copilot'],row['fsm'],row['fa1'],row['fa2'])
            voy.append(v) #Lesid ur UpcomingFlights i listann voy
#Farid i gegnum oll flug i UpcomingFlights og departure timi borinn saman vid departure tima a flugi sem verid er ad baeta inn, ef their eru their somu er boolAirportOccupied breytt i True
            if v.departingFrom == 'KEF' and (v.departure == newDateDep or v.departure == newDateRet):
                print("The airport is already occupied")
                boolAirportOccupied=True
            elif v.arrivingAt == 'KEF' and (v.arrival == newDateDep or v.arrival == newDateRet):
                print("The airport is already occupied")
                boolAirportOccupied=True

    File1.close()
    if boolAirportOccupied==False:
        voy.append(depFlight)
        voy.append(retFlight)
        #Nyju flugunum er baett vid ef flugvollurinn er ekki fratekinn
    return voy
