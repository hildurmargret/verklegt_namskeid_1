
import csv
from LogicLayer.Date import*
from ModelClasses.Voyage import*
from ModelClasses.flightRoute import*
from LogicLayer.leitaVoyage import*
from collections import OrderedDict

def voyageByWeek(inpt, inpt_year):


    daterange = getDateRangeFromWeek(inpt, inpt_year)

    nytdag=add_day(daterange[0],1)

    voyages = []

    today=now()

    if today>daterange[1]:
        file='PastFlights copy.csv'
    else:
        file='UpcomingFlights copy3.csv'

    #file_flights=OpenFile(file)
    allFlights=read_pastFlights(file)
    tel=0
    flug=[]
    dep=[]
    flug2=[]

    for i in range(len(allFlights)):
        if daterange[1] <= allFlights[i].departure < nytdag:
            dep.append(allFlights[i].departure)

            voyage = leitaVoyage(allFlights[i].flightNumber)

            if tel%2 != 0:
                voyages.extend(voyage)
            tel=tel+1
    for i in range(len(voyages)):
        for j in range(len(dep)):
            if voyages[i].departureFlight.departure == dep[j]:
                flug.append(voyages[i])

    seen = set()
    flug2 = [x for x in flug if x.departureFlight.departure not in seen and not seen.add(x.departureFlight.departure)]


    #print(len(voyages))
        #print(voyages[1].returnFlight.flightNumber)
    return flug2, daterange
