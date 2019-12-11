
import csv
from LogicLayer.Date import*
from ModelClasses.Voyage import*
from ModelClasses.flightRoute import*
from LogicLayer.leitaVoyage import*

def voyageByWeek(inpt, inpt_year):


    daterange = getDateRangeFromWeek(inpt, inpt_year)
    ar=getYear(daterange[0])
    man=getMonth(daterange[0])
    dag=getDay(daterange[0])
    klst=getHour(daterange[0])
    min=getMinute(daterange[0])
    # nyt=getDate(ar,man,dag,klst,min)
    # print(type(nyt))
    # lokad=add_day(ar,man,dag,klst,min)
    # print(lokad)
    nytdag=add_hour("2019-11-30T00:00:00",3)
    print(nytdag)


    voyages = []
    #retVoyages = []

    today=now()

    if today>daterange[1]:
        file='PastFlights.csv'
    else:
        file='UpcomingFlights copy3.csv'

    file_flights=OpenFile(file)
    allFlights=read_pastFlights(file_flights)
    tel=0

    for i in range(len(allFlights)):
        if daterange[1] <= allFlights[i].departure and daterange[0] >= allFlights[i].departure:
            voyage = leitaVoyage(allFlights[i].flightNumber)
            if tel%2 != 0:
                voyages.append(voyage)
            tel=tel+1

    return voyages
