from DataLayer.OpenFile import*
from ModelClasses.Destination import*
import csv

def getDestinations():

    Destination_array = []
    fjoldiAfStad=[]
    listOfDest=[]

    FileOpen = OpenFile("DestinationsCopy.csv")
    with FileOpen as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Destination = row['destination']
            Destination_array.append(Destination)
            Dest=CreateDestination(row["id"],row['destination'], row['country'], row['distance'], row['contactName'], row['contactNumber'])
            listOfDest.append(Dest)

    listOfDest.sort(key=lambda dest: dest.destination)

    return listOfDest
