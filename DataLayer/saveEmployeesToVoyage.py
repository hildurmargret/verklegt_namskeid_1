import csv
from ModelClasses.Voyage import*
def employeesToVoyage(voyage,Employee):
    voy=[]
    path="/Users/palinakroyer/github/verklegt_namskeid_1/csvFiles/UpcomingFlights copy.csv"
    f=open(path, 'w')

    writer = csv.writer(f)
    writer.writerow( ('flightNumber','departingFrom','arrivingAt','departure','arrival','Captain','copilot','fsm','fa1','fa2') )
    with open(path,'r') as File1:
        csv_reader = csv.DictReader(File1)
        for row in csv_reader:
            v = createVoyage(row['flightNumber'],row['departingFrom'],row['arrivingAt'],row['departure'],row['arrival'],row['Captain'],row['copilot'],row['fsm'],row['fa1'],row['fa2'])
            voy.append(v)
            print(voy)
    File1.close()


    for i in range(len(voyage)):
        print("HIII")
        if voy[i].fligheNumber==voyage.flightNumber:
            if Employee.rank=="Captain":
                if voyage.Captain=="":
                    voyage.Captain=Employee.SSN
                else:
                    print("There is already a captain")
            elif Employee.rank=="Copilot":
                if voyage.Copilot=="":
                    voyage.Copilot=Employee.SSN
                else:
                    print("There is already a copilot")
            elif Employee.rank=="Flight Attendant":
                if voyage.fa1=="":
                    voyage.fa1=Employee.SSN
                elif voyage.fa2=="":
                    voyage.fa2=Employee.SSN
                else:
                    print("There are already two flight attendants ")
            elif Employee.rank=="Flight Service Manager":
                if voyage.fsm=="":
                    voyage.fsm=Employee.SSN
                else:
                    print("There is already a flight service manager")
            writer.writerow((voyage.fligheNumber,voyage.departingFrom,voyage.arrivingAt,voyage.departure,voyage.arrival,voyage.Captain,voyage.copilot,voyage.fsm,voyage.fa1,voyage.fa2))
        else:
            writer.writerow((voy[i].fligheNumber,voy[i].departingFrom,voy[i].arrivingAt,voy[i].departure,voy[i].arrival,voy[i].Captain,voy[i].copilot,voy[i].fsm,voy[i].fa1,voy[i].fa2))
