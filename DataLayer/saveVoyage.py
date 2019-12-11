from ModelClasses.Voyage import*
def saveVoyageInFile(newVoyage):
    depFlight=newVoyage.departureFlight
    retFlight=newVoyage.returnFlight
    path="/Users/palinakroyer/github/verklegt_namskeid_1/csvFiles/UpcomingFlights copy.csv"
    f=open(path, "a")
    # print(type(newVoyage))
    # print(newVoyage.departureFlight.departingFrom)
    # print(depFlight.arrivingAt)
    # print(depFlight.departure)
    # print(depFlight.arrival)
    # print(newVoyage.returnFlight.departingFrom)
    # print(retFlight.arrivingAt)
    # print(retFlight.departure)
    # print(retFlight.arrival)
    f.write(depFlight.flightNumber+","+depFlight.departingFrom+","+depFlight.arrivingAt+","+depFlight.departure+","+depFlight.arrival+"\n")
    f.write(retFlight.flightNumber+","+retFlight.departingFrom+","+retFlight.arrivingAt+","+retFlight.departure+","+retFlight.arrival+"\n")
