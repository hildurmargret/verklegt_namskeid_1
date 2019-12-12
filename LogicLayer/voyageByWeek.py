
import csv
from LogicLayer.Date import*
from ModelClasses.Voyage import*
from ModelClasses.flightRoute import*
from LogicLayer.leitaVoyage import*
from collections import OrderedDict

def voyageByWeek(inpt, inpt_year):


    daterange = getDateRangeFromWeek(inpt, inpt_year)
    # ar=getYear(daterange[0])
    # man=getMonth(daterange[0])
    # dag=getDay(daterange[0])
    # klst=getHour(daterange[0])
    # min=getMinute(daterange[0])
    # nyt=getDate(ar,man,dag,klst,min)
    # print(type(nyt))
    # lokad=add_day(ar,man,dag,klst,min)
    # print(lokad)
    nytdag=add_day(daterange[0],1)
    #print(daterange)
    #print(nytdag)
    #print(nytdag)


    voyages = []
    #retVoyages = []

    today=now()

    if today>daterange[1]:
        file='PastFlights copy.csv'
    else:
        file='UpcomingFlights copy3.csv'

    file_flights=OpenFile(file)
    allFlights=read_pastFlights(file_flights)
    tel=0
    flug=[]
    dep=[]
    flug2=[]

    for i in range(len(allFlights)):
        if daterange[1] <= allFlights[i].departure < nytdag:
            dep.append(allFlights[i].departure)
            #print(allFlights[i].departure)
            #flug.append(allFlights[i])
            voyage = leitaVoyage(allFlights[i].flightNumber)
            #voyages.extend(voyage)
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
