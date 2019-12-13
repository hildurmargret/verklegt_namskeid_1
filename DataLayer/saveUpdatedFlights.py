import csv
def updateFlights(flights, file):

    #fall sem skrifar inn uppfærðar upplýsingar um flight

    staff=[]
    path="/Users/valdisbaerings/Documents/github/verklegt_namskeid_1/csvFiles/" + file

    f=open(path, 'w')

    writer = csv.writer(f)
    writer.writerow( ('flightNumber', 'departingFrom', 'arrivingAt','departure','arrival','aircraftID', 'soldTickets','captain','copilot','fsm','fa1','fa2') )

    for i in range(len(flights)):
        writer.writerow((flights[i].flightNumber,flights[i].departingFrom,flights[i].arrivingAt,flights[i].departure,flights[i].arrival,flights[i].aircraftId,flights[i].soldTickets,flights[i].captain,flights[i].copilot,flights[i].fsm,flights[i].fa1,flights[i].fa2))

    f.close()
