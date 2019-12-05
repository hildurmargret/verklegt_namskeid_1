import csv

def listAllDestinationsAlph():
    path='/Users/SaraLind/github/verklegt_namskeid_1/Documents/github/Verklegt1/UPDATEDSTUDENTDATA/'
    skra='Destinations.csv'

    file = path + skra
    Destination_array = []
    fjoldiAfStad=[]

    with open(file,'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Destination = row['destination']
            Destination_array.append(Destination)
            Destination_array.sort()

    counter = 0
    for i in range(len(Destination_array)):
        print(Destination_array[i])
