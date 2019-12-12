
import csv
from LogicLayer.Date import*
from ModelClasses.flightRoute import*
from DataLayer.read_pastFlights import *
from DataLayer.OpenFile import *

def voyageByDate(inptDate):

    inptDay = str(inptDate[0:2])
    inptMonth = str(inptDate[3:5])
    inptYear = str(inptDate[6:10])

    stdDate=inptYear + '-'+ inptMonth + '-' + inptDay + 'T' + '00:00:00'

    #print(stdDate)

    today=now()

    if today>stdDate:
        file='PastFlights copy.csv'
    else:
        file='UpcomingFlights copy3.csv'

    #print(file)

    file_flights=OpenFile(file)
    allFlights=read_pastFlights(file_flights)

    voyRet = []
    voyDep = []
    depDay = []
    depMonth = []
    depYear = []
    depMinute = []
    depHour = []
    arrDay = []
    arrMonth = []
    arrYear = []
    arrMinute = []
    arrHour = []
    tel=0

    #print(len(allFlights))

    for i in range(len(allFlights)):

            depDay.append(str(getDay(allFlights[i].departure)))
            depMonth.append(str(getMonth(allFlights[i].departure)))
            depYear.append(str(getYear(allFlights[i].departure)))
            depMinute.append(str(getMinute(allFlights[i].departure)))
            depHour.append(str(getHour(allFlights[i].departure)))
            arrDay.append(str(getDay(allFlights[i].departure)))
            arrMonth.append(str(getMonth(allFlights[i].departure)))
            arrYear.append(str(getYear(allFlights[i].departure)))
            arrMinute.append(str(getMinute(allFlights[i].departure)))
            arrHour.append(str(getHour(allFlights[i].departure)))

            flugnr=allFlights[i].flightNumber

            no=int(flugnr[4:len(flugnr)])

            #print(no)
            #print(allFlights[i].departure)
            if stdDate[0:10] == allFlights[i].departure[0:10]: #inptDay == depDay[tel] and inptMonth == depMonth[tel] and inptYear == depYear[tel]:
                #print('hello')
                deptTime = depDay[tel] + '/' + depMonth[tel] + '/' + depYear[tel] + ' at ' + depHour[tel] + ':' + depMinute[tel]
                arvlTime = arrDay[tel] + '/' + arrMonth[tel] + '/' + arrYear[tel] + ' at ' + arrHour[tel] + ':' + arrMinute[tel]

                if no%2 == 0:
                    #voyD=createFlightRoute(allFlights[i].flightNumber, allFlights[i].departingFrom, allFlights[i].arrivingAt, deptTime, arvlTime,allFlights[i].aircraftId,allFlights[i].soldTickets, allFlights[i].captain, allFlights[i].copilot, allFlights[i].fsm, allFlights[i].fa1, allFlights[i].fa2)
                    voyD=createFlightRoute(allFlights[i].flightNumber, allFlights[i].departingFrom, allFlights[i].arrivingAt, allFlights[i].departure, allFlights[i].arrival,allFlights[i].aircraftId,allFlights[i].soldTickets, allFlights[i].captain, allFlights[i].copilot, allFlights[i].fsm, allFlights[i].fa1, allFlights[i].fa2)
                    voyDep.append(voyD)

                elif no%2 != 0:
                    voyR=createFlightRoute(allFlights[i].flightNumber, allFlights[i].departingFrom, allFlights[i].arrivingAt, allFlights[i].departure, allFlights[i].arrival, allFlights[i].aircraftId,allFlights[i].soldTickets, allFlights[i].captain, allFlights[i].copilot, allFlights[i].fsm, allFlights[i].fa1, allFlights[i].fa2)
                    voyRet.append(voyR)
            tel=tel+1

    return voyDep, voyRet
