from Date import*
def saveWS(pastDest,pastDept,pastDeptTime,pastArvlTime,upcDest,upcDept,upcDeptTime,upcArvlTime,pastFlNo,employees):
    path = '/Users/hildur/Desktop/'
    file = open(path+'WorkSchedule.txt','w')

    for k in range(len(employees)):
        file.write(employees[k])
        file.write('\n')
        file.write('PAST FLIGHTS \n')
        for j in range(len(pastFlNo)):
            file.write('Flight number: ' + pastFlNo[j] + ', From ' + pastDept[j] + ' to ' + pastDest[j] + ','),
            file.write('Departure: ' + str(getDay(pastDeptTime[j])) + '/' + str(getMonth(pastDeptTime[j])) + '/' + str(getYear(pastDeptTime[j])) + ' at ' + str(getHour(pastDeptTime[j])) + ':' + str(getMinute(pastDeptTime[j])) + ','),
            file.write('Arrival: ' + str(getDay(pastArvlTime[j])) + '/' + str(getMonth(pastArvlTime[j])) + '/' + str(getYear(pastArvlTime[j])) + ' at ' + str(getHour(pastArvlTime[j])) + ':' + str(getMinute(pastArvlTime[j])) + '\n')
        file.write('\n')

        file.write('UPCOMING FLIGHTS \n')
        for j in range(len(pastFlNo)):
            file.write('Flight number: ' + pastFlNo[j] + ', From ' + pastDept[j] + ' to ' + pastDest[j] + ','),
            file.write('Departure: ' + str(getDay(pastDeptTime[j])) + '/' + str(getMonth(pastDeptTime[j])) + '/' + str(getYear(pastDeptTime[j])) + ' at ' + str(getHour(pastDeptTime[j])) + ':' + str(getMinute(pastDeptTime[j])) + ','),
            file.write('Arrival: ' + str(getDay(pastArvlTime[j])) + '/' + str(getMonth(pastArvlTime[j])) + '/' + str(getYear(pastArvlTime[j])) + ' at ' + str(getHour(pastArvlTime[j])) + ':' + str(getMinute(pastArvlTime[j])) + '\n')
            """print('Flight number: ' + upcFlNo[j] + ', From ' + upcDept[j] + ' to ' + upcDest[j] + ','),
            print('Departure: ' + str(getDay(upcDeptTime[j])) + '/' + str(getMonth(upcDeptTime[j])) + '/' + str(getYear(upcDeptTime[j])) + ' at ' + str(getHour(upcDeptTime[j])) + ':' + str(getMinute(upcDeptTime[j])) + ','),
            print('Arrival: ' + str(getDay(upcArvlTime[j])) + '/' + str(getMonth(upcArvlTime[j])) + '/' + str(getYear(upcArvlTime[j])) + ' at ' + str(getHour(upcArvlTime[j])) + ':' + str(getMinute(upcArvlTime[j])))"""
        file.write('\n')
        file.write('-----------------------------------------------------------------------------------------------------')
        file.write('\n')

    file.close()
