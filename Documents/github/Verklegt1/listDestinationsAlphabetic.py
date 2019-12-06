from OpenFile import*

import csv

def listAllDestinationsAlph():

    #file = path + skra
    Destination_array = []
    fjoldiAfStad=[]

    FileOpen = OpenFile("Destinations.csv")
    with FileOpen as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Destination = row['destination']
            Destination_array.append(Destination)
            Destination_array.sort()


    for i in range(len(Destination_array)):
        print(Destination_array[i])
