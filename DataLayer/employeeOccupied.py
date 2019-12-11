import csv
from LogicLayer.Date import*
from ModelClasses.flightRoute import*
from DataLayer.OpenFile import *

def employeeOccupied(employee,retRoute):
    date1=getDay(retRoute.departure)
    file='UpcomingFlights copy.csv'
    file_=openFile(file)

    #path="/Users/palinakroyer/github/verklegt_namskeid_1/csvFiles/UpcomingFlights copy.csv"
    with file_ as File1:
        #print("HIII")
        csv_reader = csv.DictReader(File1)
        for row in csv_reader:
            v = createFlightRoute(row['flightNumber'],row['departingFrom'],row['arrivingAt'],row['departure'],row['arrival'],"",row['captain'],row['copilot'],row['fsm'],row['fa1'],row['fa2'])
            date2=getDay(v.departure)
            #print(date1)
            #print(date2)
            #print(employee.SSN)
            if date2==date1:
                if employee.SSN==v.captain:
                    return True
                if employee.SSN==v.copilot:
                    return True
                if employee.SSN==v.fsm:
                    return True
                if employee.SSN==v.fa1:
                    return True
                if employee.SSN==v.fa2:
                    return True
    return False
