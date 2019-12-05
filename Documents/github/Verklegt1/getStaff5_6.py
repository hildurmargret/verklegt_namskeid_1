# defstaffInfo2(inp):

import csv
from leitaStaff import leitaStaff
from printWorkSchedule import*
from saveWorkSchedule import*
from Date import*

path='/Users/hildur/Documents/github/verklegt_namskeid_1/Documents/github/Verklegt1/UPDATEDSTUDENTDATA/'
skra1='PastFlights.csv'
file1=path+skra1

skra2='Crew.csv'
file2=path+skra2
file3=path+'UpcomingFlights.csv'

inpt='son'
number = 6
ssn=[]
rank=[]
pastDest=[]
pastDept=[]
pastDeptTime=[]
pastArvlTime=[]
upcDest=[]
upcDept=[]
upcDeptTime=[]
upcArvlTime=[]
pastFlNo=[]
employees=[]
fjoldiAfStad=[]

with open(file2,'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        ssn,rank=leitaStaff(inpt,file2,ssn,rank)
        for i in range(len(ssn)):
            if row['ssn']==ssn[i]:
                if row['role'] == 'Cabincrew':
                    employees.append(row['ssn'] + ', ' +row['name']+', '+row['role']+', '+row['rank'] + ', ' + row['address'] + ', ' + row['phonenumber'])
                else:
                    employees.append(row['ssn'] + ', ' +row['name']+', '+row['role']+', '+row['rank'] + ', ' + row['licence'] + ', ' + row['address'] + ', ' + row['phonenumber'])
                break

"""#Upcoming flights
for i in range(len(employees)):
    with open(file3,'r') as csvFile:
        reader=csv.DictReader(csvFile)
        for row in reader:
            if rank[i]=='Flight Attendant' and ssn[i] in (row['fa1'] or row['fa2']):
                upcDeptTime.append(row['departure'])
                upcArvlTime.append(row['arrival'])
                upcFlNo.append(row['flightNumber'])
                upcDest.append(row['arrivingAt'])
                upcDept.append(row['departingFrom'])
            elif rank[i]=='Flight Service Manager' and ssn[i] in row['fsm']:
                upcDeptTime.append(row['departure'])
                upcArvlTime.append(row['arrival'])
                upcFlNo.append(row['flightNumber'])
                upcDest.append(row['arrivingAt'])
                upcDept.append(row['departingFrom'])
            elif rank[i]=='Captain' and ssn[i] in row['captain']:
                upcDeptTime.append(row['departure'])
                upcArvlTime.append(row['arrival'])
                upcFlNo.append(row['flightNumber'])
                upcDest.append(row['arrivingAt'])
                upcDept.append(row['departingFrom'])
            elif rank[i]=='Copilot' and ssn[i] in row['copilot']:
                upcDeptTime.append(row['departure'])
                upcArvlTime.append(row['arrival'])
                upcFlNo.append(row['flightNumber'])
                upcDest.append(row['arrivingAt'])
                upcDept.append(row['departingFrom'])"""

#Past flights
for i in range(len(employees)):
    with open(file1,'r') as csvFile:
        reader=csv.DictReader(csvFile)
        for row in reader:
            if rank[i]=='Flight Attendant' and ssn[i] in (row['fa1'] or row['fa2']):
                pastDeptTime.append(row['departure'])
                pastArvlTime.append(row['arrival'])
                pastFlNo.append(row['flightNumber'])
                pastDest.append(row['arrivingAt'])
                pastDept.append(row['departingFrom'])
            elif rank[i]=='Flight Service Manager' and ssn[i] in row['fsm']:
                pastDeptTime.append(row['departure'])
                pastArvlTime.append(row['arrival'])
                pastFlNo.append(row['flightNumber'])
                pastDest.append(row['arrivingAt'])
                pastDept.append(row['departingFrom'])
            elif rank[i]=='Captain' and ssn[i] in row['captain']:
                pastDeptTime.append(row['departure'])
                pastArvlTime.append(row['arrival'])
                pastFlNo.append(row['flightNumber'])
                pastDest.append(row['arrivingAt'])
                pastDept.append(row['departingFrom'])
            elif rank[i]=='Copilot' and ssn[i] in row['copilot']:
                pastDeptTime.append(row['departure'])
                pastArvlTime.append(row['arrival'])
                pastFlNo.append(row['flightNumber'])
                pastDest.append(row['arrivingAt'])
                pastDept.append(row['departingFrom'])

        fjoldiAfStad.append(len(pastDest))

if number == 5:
    counter = 0
    for j in range(len(fjoldiAfStad)):
        print employees[j]
        for i in range(fjoldiAfStad[j]-counter):
            if pastDest[i+counter]!='KEF':
                print(str(getDay(pastDeptTime[j])) + '/' + str(getMonth(pastDeptTime[j])) + '/' + str(getYear(pastDeptTime[j])) + ': '+ pastDest[i+counter])
        counter=fjoldiAfStad[j]
        print
elif number == 6:
    save = printWS(pastDest, pastDept, pastDeptTime, pastArvlTime, upcDest, upcDept, upcDeptTime, upcArvlTime, pastFlNo,employees)
    if save == 1:
        saveWS(pastDest, pastDept, pastDeptTime, pastArvlTime, upcDest, upcDept, upcDeptTime, upcArvlTime, pastFlNo,employees)
