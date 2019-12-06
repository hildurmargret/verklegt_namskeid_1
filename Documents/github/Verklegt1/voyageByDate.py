
import csv
from Date import*

def voyageByDate():

    inptDate = '20/12/2019'
    inptDay = str(inptDate[0:2])
    inptMonth = str(inptDate[3:5])
    inptYear = str(inptDate[6:10])

    path='/Users/valdisbaerings/Documents/verklegt_namskeid_1/Documents/github/Verklegt1/UPDATEDSTUDENTDATA/'

    file1=path+'PastFlights.csv'
    file2=path+'UpcomingFlights copy.csv'

    voyage = []
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
    fjoVi=0

    with open(file2,'r') as csv_file:
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
                    voyDep.append(row['flightNumber'] + ', ' + row['departingFrom'] + ', ' + row['arrivingAt'] + ', Departure: ' + deptTime + ', Arrival: ' + arvlTime)
                    voyage.append(voyDep)

                elif no%2 != 0:
                    voyRet.append(row['flightNumber'] + ', ' + row['departingFrom'] + ', ' + row['arrivingAt'] + ', Departure: ' + deptTime + ', Arrival: ' + arvlTime)
                    voyage.append(voyRet)
            tel=tel+1

    return voyDep, voyRet

dep, ret = voyageByDate()

for i in range(len(dep)):
    print('VOYAGE DEPARTURE')
    print dep[i]
    print('VOYAGE RETURN')
    print ret[i]
    print

#VANTAR HINN FILE
