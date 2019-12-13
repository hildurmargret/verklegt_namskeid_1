from DataLayer.OpenFile import *
from DataLayer.read_pastFlights import *
from ModelClasses.flightRoute import *
from LogicLayer.Date import *

def airplaneInUse(input_date, input_time):

    inptDay = str(input_date[0:2])
    inptMonth = str(input_date[3:5])
    inptYear = str(input_date[6:10])

    stdInptDate = inptYear + '-' + inptMonth + '-' + inptDay + 'T' + input_time

    today=now()

    #fer inni viðeigandi skra
    if today>stdInptDate:
        file='PastFlights copy.csv'
    else:
        file='UpcomingFlights copy3.csv'

    allFlights=read_pastFlights(file)

    inAir=[]
    onGround=[]

    #tvær klst aftur i timann þvi ef flug tok af stað þa þa er það inAir
    timabil=add_hour(stdInptDate, (-2))

    #fer gegnum öll flug og tekka hvort timasetningin og dags passi við
    for i in range(len(allFlights)):
        if inptDay == str(getDay(allFlights[i].departure)) and inptMonth == str(getMonth(allFlights[i].departure)) and inptYear == str(getYear(allFlights[i].departure)):
            #tekka hvort flugvel se i loftinu
            if timabil < allFlights[i].departure and allFlights[i].departure <= stdInptDate:
                air=createFlightRoute(allFlights[i].flightNumber, allFlights[i].departingFrom,allFlights[i].arrivingAt, allFlights[i].departure, allFlights[i].arrival, allFlights[i].aircraftId, allFlights[i].captain, allFlights[i].copilot, allFlights[i].fsm, allFlights[i].fa1, allFlights[i].fa2)
                inAir.append(air)
            else:
                onGr=createFlightRoute(allFlights[i].flightNumber, allFlights[i].departingFrom, allFlights[i].arrivingAt,  allFlights[i].departure, allFlights[i].arrival, allFlights[i].aircraftId, allFlights[i].captain, allFlights[i].copilot, allFlights[i].fsm, allFlights[i].fa1, allFlights[i].fa2)
                onGround.append(onGr)
    #skila bæði flugvelum i lofti og þeim sem eru ekki
    return inAir, onGround
