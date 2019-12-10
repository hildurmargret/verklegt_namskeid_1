import csv
from ModelClasses.flightRoute import*
def employeesToVoyage(voyage,Employee):
    voy=[]

    path="/Users/palinakroyer/github/verklegt_namskeid_1/csvFiles/UpcomingFlights copy.csv"



    with open(path,'r') as File1:
        csv_reader = csv.DictReader(File1)
        for row in csv_reader:
            v = createFlightRoute(row['flightNumber'],row['departingFrom'],row['arrivingAt'],row['departure'],row['arrival'],row['captain'],row['copilot'],row['fsm'],row['fa1'],row['fa2'])
            voy.append(v)
    File1.close()
    f=open(path, 'w')
    writer = csv.writer(f)
    writer.writerow( ('flightNumber','departingFrom','arrivingAt','departure','arrival','captain','copilot','fsm','fa1','fa2') )

    for i in range(len(voy)):

        if voy[i].flightNumber==voyage.departureFlight.flightNumber:
            print("jii")
            print(Employee.SSN)
            if Employee.rank=="Captain":
                if voyage.departureFlight.captain=="":
                    voyage.departureFlight.captain=Employee.SSN
                else:
                    print("There is already a captain")
            elif Employee.rank=="Copilot":
                if voyage.departureFlight.copilot=="":
                    voyage.departureFlight.copilot=Employee.SSN
                else:
                    print("There is already a copilot")
            elif Employee.rank=="Flight Attendant":
                print(voyage.departureFlight.fa1)
                if voyage.departureFlight.fa1=="":
                    voyage.departureFlight.fa1=Employee.SSN
                elif voyage.departureFlight.fa2=="":
                    voyage.departureFlight.fa2=Employee.SSN
                else:
                    print("There are already two flight attendants ")
            elif Employee.rank=="Flight Service Manager":
                if voyage.departureFlight.fsm=="":
                    voyage.departureFlight.fsm=Employee.SSN
                else:
                    print("There is already a flight service manager")
            writer.writerow((voyage.departureFlight.flightNumber,voyage.departureFlight.departingFrom,voyage.departureFlight.arrivingAt,voyage.departureFlight.departure,voyage.departureFlight.arrival,voyage.departureFlight.captain,voyage.departureFlight.copilot,voyage.departureFlight.fsm,voyage.departureFlight.fa1,voyage.departureFlight.fa2))
        else:
            writer.writerow((voy[i].flightNumber,voy[i].departingFrom,voy[i].arrivingAt,voy[i].departure,voy[i].arrival,voy[i].captain,voy[i].copilot,voy[i].fsm,voy[i].fa1,voy[i].fa2))
    f.close()
