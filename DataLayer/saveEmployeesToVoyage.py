# import csv
# from ModelClasses.flightRoute import*
# from LogicLayer.Date import*
# from DataLayer.employeeOccupied import*
# def employeesToVoyage(voyage,Employee):
#     voy=[]
#     path="/Users/hildur/Documents/github/verklegt_namskeid_1/csvFiles/UpcomingFlights copy3.csv"
#     departRoute=voyage.departureFlight
#     retRoute=voyage.returnFlight
#     date=getDay(retRoute.departure)
#     #emplOccupied=employeeOccupied(Employee,retRoute)
# 
#     # print(departRoute.aircraftId)
#     with open(path,'r') as File1:
#         csv_reader = csv.DictReader(File1)
#         for row in csv_reader:
#             v = createFlightRoute(row['flightNumber'],row['departingFrom'],row['arrivingAt'],row['departure'],row['arrival'],row['aircraftID'],row['soldTickets'],row['captain'],row['copilot'],row['fsm'],row['fa1'],row['fa2'])
#             voy.append(v)
#     File1.close()
#     f=open(path, 'w')
#     writer = csv.writer(f)
#     writer.writerow( ('flightNumber','departingFrom','arrivingAt','departure','arrival','aircraftID','soldTickets','captain','copilot','fsm','fa1','fa2') )
#     for i in range(len(voy)):
#
#         if voy[i].flightNumber==departRoute.flightNumber:
#
#             captain_bool = 0
#             copilot_bool = 0
#             fsm_bool = 0
#
#             if Employee.rank=="Captain":
#                 if (departRoute.captain=="")&(emplOccupied==False)&(voy[i].aircraftId==Employee.licence):
#                     departRoute.captain=Employee.SSN
#                     retRoute.captain=Employee.SSN
#                 elif departRoute.captain!="":
#                     print("There is already a captain")
#                 elif emplOccupied==True:
#                     print("The employee is not available")
#                 elif voy[i].aircraftId!=Employee.licence:
#                     print("The captain does not have the required licence")
#
#             elif (Employee.rank=="Copilot"):
#                 if (departRoute.copilot=="")&(emplOccupied==False)&(voy[i].aircraftId==Employee.licence):
#                     departRoute.copilot=Employee.SSN
#                     retRoute.copilot=Employee.SSN
#                 elif departRoute.captain!="":
#                     print("There is already a copilot")
#                 elif emplOccupied==True:
#                     print("The employee is not available")
#                 elif voy[i].aircraftId!=Employee.licence:
#                     print("The copilot does not have the required licence")
#             elif Employee.rank=="Flight Attendant":
#                 if departRoute.fa1=="":
#                     departRoute.fa1=Employee.SSN
#                     retRoute.fa1=Employee.SSN
#                 elif departRoute.fa2=="":
#                     departRoute.fa2=Employee.SSN
#                     retRoute.fa2=Employee.SSN
#                 else:
#                     print("There are already two flight attendants ")
#             elif Employee.rank=="Flight Service Manager":
#                 if departRoute.fsm=="":
#                     departRoute.fsm=Employee.SSN
#                     retRoute.fsm=Employee.SSN
#                 else:
#                     print("There is already a flight service manager")
#             writer.writerow((departRoute.flightNumber,departRoute.departingFrom,departRoute.arrivingAt,departRoute.departure,departRoute.arrival,departRoute.aircraftId,departRoute.soldTickets,departRoute.captain,departRoute.copilot,departRoute.fsm,departRoute.fa1,departRoute.fa2))
#         elif voy[i-1].flightNumber==(departRoute.flightNumber):
#             writer.writerow((retRoute.flightNumber,retRoute.departingFrom,retRoute.arrivingAt,retRoute.departure,retRoute.arrival,retRoute.aircraftId,retRoute.soldTickets,retRoute.captain,retRoute.copilot,retRoute.fsm,retRoute.fa1,retRoute.fa2))
#         else:
#             writer.writerow((voy[i].flightNumber,voy[i].departingFrom,voy[i].arrivingAt,voy[i].departure,voy[i].arrival,voy[i].aircraftId,voy[i].soldTickets,voy[i].captain,voy[i].copilot,voy[i].fsm,voy[i].fa1,voy[i].fa2))
#     f.close()
