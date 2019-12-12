from ModelClasses.Destination import*
def saveDestinationInFile(newDest):
    path="/Users/hildur/Documents/github/verklegt_namskeid_1/csvFiles/DestinationsCopy.csv"
    f=open(path, "a")
    f.write(newDest.id+","+newDest.destination+","+newDest.country+","+newDest.distance+","+newDest.contactName+","+newDest.contactNumber+"\n")
