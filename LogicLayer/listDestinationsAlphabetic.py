from DataLayer.OpenFile import*
from ModelClasses.Destination import*
import csv

def listAllDestinationsAlph():

    Destination_array = []
    fjoldiAfStad=[]
    listOfDest=[]

    FileOpen = OpenFile("Destinations.csv")
    with FileOpen as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Destination = row['destination']
            Destination_array.append(Destination)
            Destination_array.sort()
            Dest=CreateDestination(row["id"],row['destination'])
            listOfDest.append(Dest)
    for i in range(len(Destination_array)):
        print(Destination_array[i])
    return listOfDest
