from ModelClasses.Voyage import*
def saveVoyageInFile(newVoyage):
    path="/Users/SaraLind/github/verklegt_namskeid_1/csvFiles/UpcomingFlights copy.csv"
    f=open(path, "a")
    f.write(newVoyage.flightNumber+","+newVoyage.departingFrom+","+newVoyage.arrivingAt+","+newVoyage.departure+","+newVoyage.arrival+"\n")
