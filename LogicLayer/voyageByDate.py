
import csv
from LogicLayer.Date import*
from ModelClasses.Voyage import*

def voyageByDate(inptDate):

    #inptDate = '20/12/2019'
    inptDay = str(inptDate[0:2])
    inptMonth = str(inptDate[3:5])
    inptYear = str(inptDate[6:10])

    stdDate=inptYear + '-'+ inptMonth + '-' + inptDay + 'T' + '00:00:00'

    today=now()

    if today>stdDate:
        file='PastFlights.csv'
    else:
        file='UpcomingFlights copy.csv'

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

            if inptDay == depDay[tel] and inptMonth == depMonth[tel] and inptYear == depYear[tel]:
                deptTime = depDay[tel] + '/' + depMonth[tel] + '/' + depYear[tel] + ' at ' + depHour[tel] + ':' + depMinute[tel]
                arvlTime = arrDay[tel] + '/' + arrMonth[tel] + '/' + arrYear[tel] + ' at ' + arrHour[tel] + ':' + arrMinute[tel]

                if no%2 == 0:
                    voyD=createVoyage(row['flightNumber'], row['departingFrom'], row['arrivingAt'], deptTime, arvlTime,0,0)
                    voyDep.append(voyD)

                elif no%2 != 0:
                    voyR=createVoyage(row['flightNumber'], row['departingFrom'], row['arrivingAt'], deptTime, arvlTime,0,0)
                    voyRet.append(voyR)
            tel=tel+1

    return voyDep, voyRet

#dep, ret = voyageByDate()
