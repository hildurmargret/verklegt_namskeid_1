
import csv
from LogicLayer.Date import*
from ModelClasses.Voyage import*
from ModelClasses.flightRoute import*
from LogicLayer.leitaVoyage import*

def voyageByWeek(inpt, inpt_year):


    daterange = getDateRangeFromWeek(inpt, inpt_year)
    print(daterange)

    voyages = []
    #retVoyages = []

    today=now()

    if today>daterange[1]:
        file='PastFlights.csv'
    else:
        file='UpcomingFlights copy3.csv'

    file_flights=OpenFile(file)
    allFlights=read_pastFlights(file_flights)

    for i in range(len(allFlights)):
        if daterange[1] <= allFlights[i].departure and daterange[0] >= allFlights[i].departure:
            voyage = leitaVoyage(allFlights[i].flightNumber)
            voyages.append(voyage)

    return voyages
