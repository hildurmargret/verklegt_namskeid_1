import csv
def updateFlights(flights):

    staff=[]
    path="/Users/hildur/Documents/github/verklegt_namskeid_1/csvFiles/UpcomingFlights copy3.csv"

    f=open(path, 'w')

    writer = csv.writer(f)
    writer.writerow( ('flightNumber', 'departingFrom', 'arrivingAt','departure','arrival','aircraftID','captain','copilot','fsm','fa1','fa2') )
    print(len(flights))
    for i in range(len(flights)):
        writer.writerow((flights[i].flightNumber,flights[i].departingFrom,flights[i].arrivingAt,flights[i].departure,flights[i].arrival,flights[i].aircraftId,flights[i].captain,flights[i].copilot,flights[i].fsm,flights[i].fa1,flights[i].fa2))
