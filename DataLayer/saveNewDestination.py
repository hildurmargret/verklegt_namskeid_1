from ModelClasses.Destination import*
import sys
import os
def saveDestinationInFile(newDest):
    ##path="/Users/hildur/Documents/github/verklegt_namskeid_1/csvFiles/DestinationsCopy.csv"

    absPathFile = os.path.abspath(__file__)
    fileDir = os.path.dirname(os.path.abspath(__file__))
    parentDir = os.path.dirname(fileDir)
    path = parentDir + "/csvFiles/DestinationsCopy.csv"

    f=open(path, "a")
    f.write(newDest.id+","+newDest.destination+","+newDest.country+","+newDest.distance+","+newDest.contactName+","+newDest.contactNumber+"\n")
