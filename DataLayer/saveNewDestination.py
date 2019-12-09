from ModelClasses.Destination import*
def saveDestinationInFile(newDest):
    path="/Users/SaraLind/github/verklegt_namskeid_1/DestinationsCopy.csv"
    f=open(path, "a")
    f.write(newDest.airport+","+newDest.country+","+newDest.contactName+","+newDest.contactNumber+"\n")

    
