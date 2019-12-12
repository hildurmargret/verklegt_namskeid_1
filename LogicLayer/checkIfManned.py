import csv
from LogicLayer.Date import*
from DataLayer.OpenFile import*
from DataLayer.read_pastFlights import *

def checkIfManned(voyage):

    flNo = voyage.flightNumber

    today=now()


    #path = '/Users/valdisbaerings/Documents/github/verklegt_namskeid_1/csvFiles/'

    if today>voyage.departure:
        file='PastFlights copy.csv'
    else:
        file='UpcomingFlights copy3.csv'

    file_flights=OpenFile(file)
    allFlights=read_pastFlights(file_flights)

    captain_bool = 0
    copilot_bool = 0
    fsm_bool = 0

    for i in range(len(allFlights)):
        if allFlights[i].flightNumber == flNo:
            #if 'captain' in row:
            if allFlights[i].captain: # is not None:
                captain_bool = 1
        #if 'copilot' in row:
            if allFlights[i].copilot: # is not None:
                copilot_bool = 1
        #if 'fsm' in row:
            if allFlights[i].fsm: # is not None:
                fsm_bool = 1

    return captain_bool, copilot_bool, fsm_bool
