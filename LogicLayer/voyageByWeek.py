
import csv
from LogicLayer.Date import*
from ModelClasses.Voyage import*
from ModelClasses.flightRoute import*
from LogicLayer.leitaVoyage import*
from collections import OrderedDict

def voyageByWeek(inpt, inpt_year):

    #allir dagar innslegnar viku
    daterange = getDateRangeFromWeek(inpt, inpt_year)

    #bæti einum degi við lokadag viku til að taka voyages a lokadeginum með
    nytdag=add_day(daterange[0],1)

    voyages = []

    #athuga hvaða skra eg vil fara i
    today=now()

    if today>daterange[1]:
        file='PastFlights copy.csv'
    else:
        file='UpcomingFlights copy3.csv'

    #öll flug ur skrani
    allFlights=read_pastFlights(file)
    tel=0
    flug=[]
    dep=[]
    flug2=[]

    #fer gegnum öll flug og ef departure er a vikunni þa set eg brottfarartimann inni fallið
    #leitaVoyage sem skilar mer voyage sem passa við flugnumerið
    for i in range(len(allFlights)):
        if daterange[1] <= allFlights[i].departure < nytdag:
            dep.append(allFlights[i].departure)

            voyage = leitaVoyage(allFlights[i].flightNumber)
            #til að taka bara einu sinni hvert voyage en ekki 2
            if tel%2 != 0:
                voyages.extend(voyage)
            tel=tel+1
    #ef brottfarartimar passa saman set eg i nyjan lista
    for i in range(len(voyages)):
        for j in range(len(dep)):
            if voyages[i].departureFlight.departure == dep[j]:
                flug.append(voyages[i])

    #passa tvitelja ekki
    seen = set()
    flug2 = [x for x in flug if x.departureFlight.departure not in seen and not seen.add(x.departureFlight.departure)]

    return flug2, daterange
