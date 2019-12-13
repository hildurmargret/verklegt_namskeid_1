import csv
from LogicLayer.Date import*
from DataLayer.OpenFile import*
from DataLayer.read_pastFlights import *

def checkIfManned(voyage):

    flNo = voyage.flightNumber

    today=now()

    #fer inni viðeigandi skra
    if today>voyage.departure:
        file='PastFlights copy.csv'
    else:
        file='UpcomingFlights copy3.csv'

    allFlights=read_pastFlights(file)

    captain_bool = 0
    copilot_bool = 0
    fsm_bool = 0

    #fer gegnum öll flug og og fyrir þau sem passa við flugnumer vinnuferðarinnar og timasetningu
    for i in range(len(allFlights)):
        if allFlights[i].flightNumber == flNo and allFlights[i].departure==voyage.departure:
            #tekka hvort viðeigandi starfsmaður se skraður og skila ut bool breytum sem
            #gefa til kynna hvort svo se
            if allFlights[i].captain:
                captain_bool = 1

            if allFlights[i].copilot:
                copilot_bool = 1

            if allFlights[i].fsm:
                fsm_bool = 1

    return captain_bool, copilot_bool, fsm_bool
