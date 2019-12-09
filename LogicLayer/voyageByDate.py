
import csv
from LogicLayer.Date import*
from ModelClasses.Voyage import*

def voyageByDate(inptDate):

    #inptDate = '20/12/2019'
    inptDay = str(inptDate[0:2])
    inptMonth = str(inptDate[3:5])
    inptYear = str(inptDate[6:10])

    stdDate=inptYear + '-'+ inptMonth + '-' + inptDay + 'T' + '00:00:00'

    path='/Users/valdisbaerings/Documents/github/verklegt_namskeid_1/csvFiles/'

    today=now()

    if today>stdDate:
        file=path+'PastFlights.csv'
    else:
        file=path+'UpcomingFlights copy.csv'

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

    with open(file,'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            depDay.append(str(getDay(row['departure'])))
            depMonth.append(str(getMonth(row['departure'])))
            depYear.append(str(getYear(row['departure'])))
            depMinute.append(str(getMinute(row['departure'])))
            depHour.append(str(getHour(row['departure'])))
            arrDay.append(str(getDay(row['arrival'])))
            arrMonth.append(str(getMonth(row['arrival'])))
            arrYear.append(str(getYear(row['arrival'])))
            arrMinute.append(str(getMinute(row['arrival'])))
            arrHour.append(str(getHour(row['arrival'])))

            flugnr=row['flightNumber']

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
