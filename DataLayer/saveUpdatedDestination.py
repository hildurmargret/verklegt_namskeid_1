import csv
import sys
import os
from ModelClasses.Destination import*
def saveUpdatedDest(dest):

    #fall sem skrifar inn uppfærðar upplýsingar um destination i skrá
    Desti=[]
    ##path="/Users/valdisbaerings/Documents/github/verklegt_namskeid_1/csvFiles/DestinationsCopy.csv"

    file = OpenFile('DestinationsCopy.csv')

    with file as File1:
        csv_reader = csv.DictReader(File1)
        for row in csv_reader:
            Destination = CreateDestination(row['id'],row['destination'], row['country'], row['distance'], row['contactName'], row['contactNumber'])
            Desti.append(Destination)
    File1.close()

    absPathFile = os.path.abspath(__file__)
    fileDir = os.path.dirname(os.path.abspath(__file__))
    parentDir = os.path.dirname(fileDir)
    path = parentDir + "/csvFiles/DestinationsCopy.csv"

    f=open(path, 'w')

    writer = csv.writer(f)
    writer.writerow( ('id', 'destination', 'country', 'distance', 'contactName', 'contactNumber' ))

    for i in range(len(Desti)):
        if Desti[i].destination==dest.destination:
            writer.writerow((dest.id, dest.destination, dest.country, dest.distance, dest.contactName, dest.contactNumber))
        else:
            writer.writerow((Desti[i].id, Desti[i].destination, Desti[i].country, Desti[i].distance, Desti[i].contactName, Desti[i].contactNumber))
