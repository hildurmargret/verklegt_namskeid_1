#def emplWorking(day, month, year)
# from LogicLayer.Date import*
# import csv
#
# inptDate = '10/11/2019'
# inptDay = str(inptDate[0:2])
# inptMonth = str(inptDate[3:5])
# inptYear = str(inptDate[6:10])
#
# path='/Users/hildur/Documents/github/verklegt_namskeid_1/csvFiles/'
#
# file1=path+'PastFlights.csv'
# file2=path+'UpcomingFlights.csv'
# file3=path+'Crew.csv'
#
# emplSSN = []
# employees = []
#
# #Past flights
# with open(file1,'r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     for row in csv_reader:
#         day = str(getDay(row['departure']))
#         month = str(getMonth(row['departure']))
#         year = str(getYear(row['departure']))
#
#         if inptDay == day and inptMonth == month and inptYear == year:
#             emplSSN.append(row['captain'])
#             emplSSN.append(row['copilot'])
#             emplSSN.append(row['fsm'])
#             emplSSN.append(row['fa1'])
#             emplSSN.append(row['fa2'])
#
# #Upcoming flights
# with open(file2,'r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     for row in csv_reader:
#         day = str(getDay(row['departure']))
#         month = str(getMonth(row['departure']))
#         year = str(getYear(row['departure']))
#
#         if inptDay == day and inptMonth == month and inptYear == year:
#             emplSSN.append(row['captain'])
#             emplSSN.append(row['copilot'])
#             emplSSN.append(row['fsm'])
#             emplSSN.append(row['fa1'])
#             emplSSN.append(row['fa2'])
#
# for j in range(len(emplSSN)):
#     if j%2 != 0:
#         del emplSSN[-1]
#
# with open(file3, 'r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     for row in csv_reader:
#         for i in range(len(emplSSN)):
#             if row['ssn'] == emplSSN[i]:
#                 if row['role'] == 'Cabincrew':
#                     employees.append(row['ssn'] + ', ' +row['name']+', '+row['role']+', '+row['rank'] + ', ' + row['address'] + ', ' + row['phonenumber'])
#                 else:
#                     employees.append(row['ssn'] + ', ' +row['name']+', '+row['role']+', '+row['rank'] + ', ' + row['licence'] + ', ' + row['address'] + ', ' + row['phonenumber'])
#
# print('Employees working ' + inptDate + ':')
# for j in range(len(employees)):
#     print(employees[j])
