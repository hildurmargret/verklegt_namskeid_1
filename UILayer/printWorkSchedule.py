from LogicLayer.Date import*
def printWS(pastDest,pastDept,pastDeptTime,pastArvlTime,upcDest,upcDept,upcDeptTime,upcArvlTime,pastFlNo,employees):

    for k in range(len(employees)):
        if employees[k].role == 'Cabincrew':
            print(employees[k].name + ', ' + employees[k].SSN + ', ' + employees[k].address + ', ' + employees[k].phoneNumber + ', ' + employees[k].role + ', ' + employees[k].rank + '\n')
        else:
            print(employees[k].name + ', ' + employees[k].SSN + ', ' + employees[k].address + ', ' + employees[k].phoneNumber + ', ' + employees[k].role + ', ' + employees[k].rank + ', ' + employees[k].licence + '\n')
        print
        print('PAST FLIGHTS')
        for j in range(len(pastFlNo)):
            print('Flight number: ' + pastFlNo[j] + ', From ' + pastDept[j] + ' to ' + pastDest[j] + ', ', end = '')
            print('Departure: ' + str(getDay(pastDeptTime[j])) + '/' + str(getMonth(pastDeptTime[j])) + '/' + str(getYear(pastDeptTime[j])) + ' at ' + str(getHour(pastDeptTime[j])) + ':' + str(getMinute(pastDeptTime[j])) + ', ', end = '')
            print('Arrival: ' + str(getDay(pastArvlTime[j])) + '/' + str(getMonth(pastArvlTime[j])) + '/' + str(getYear(pastArvlTime[j])) + ' at ' + str(getHour(pastArvlTime[j])) + ':' + str(getMinute(pastArvlTime[j])))
        print

        print('UPCOMING FLIGHTS')
        for j in range(len(pastFlNo)):
            print('Flight number: ' + pastFlNo[j] + ', From ' + pastDept[j] + ' to ' + pastDest[j] + ', ', end = '')
            print('Departure: ' + str(getDay(pastDeptTime[j])) + '/' + str(getMonth(pastDeptTime[j])) + '/' + str(getYear(pastDeptTime[j])) + ' at ' + str(getHour(pastDeptTime[j])) + ':' + str(getMinute(pastDeptTime[j])) + ', ', end = '')
            print('Arrival: ' + str(getDay(pastArvlTime[j])) + '/' + str(getMonth(pastArvlTime[j])) + '/' + str(getYear(pastArvlTime[j])) + ' at ' + str(getHour(pastArvlTime[j])) + ':' + str(getMinute(pastArvlTime[j])))
            """print('Flight number: ' + upcFlNo[j] + ', From ' + upcDept[j] + ' to ' + upcDest[j] + ', ', end = '')
            print('Departure: ' + str(getDay(upcDeptTime[j])) + '/' + str(getMonth(upcDeptTime[j])) + '/' + str(getYear(upcDeptTime[j])) + ' at ' + str(getHour(upcDeptTime[j])) + ':' + str(getMinute(upcDeptTime[j])) + ', ', end = '')
            print('Arrival: ' + str(getDay(upcArvlTime[j])) + '/' + str(getMonth(upcArvlTime[j])) + '/' + str(getYear(upcArvlTime[j])) + ' at ' + str(getHour(upcArvlTime[j])) + ':' + str(getMinute(upcArvlTime[j])))"""
        print
        print('-----------------------------------------------------------------------------------------------------')
        print

        #PALINA input('Choose y to save')
    inpt = 1

    return inpt
