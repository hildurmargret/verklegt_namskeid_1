#from DataLayer.OpenFile import*
import csv

def listAllDestinationsAlph():

    #file = path + skra
    Destination_array = []
    fjoldiAfStad=[]

    path='/Users/SaraLind/github/verklegt_namskeid_1/csvFiles/'
    skra = "Destinations.csv"
    file = path+skra
    #FileOpen = OpenFile("Destinations.csv")
    with open(file,'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Destination = row['destination']
            Destination_array.append(Destination)
            Destination_array.sort()


    for i in range(len(Destination_array)):
        print(Destination_array[i])

listAllDestinationsAlph()
