import csv

#def list_all_aircraft():

path='/Users/SaraLind/github/verklegt_namskeid_1/Documents/github/Verklegt1/UPDATEDSTUDENTDATA/'
skra='Destinations.csv'

file = path + skra

with open(file,'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        Destination = row['destination']
        print(Destination)
