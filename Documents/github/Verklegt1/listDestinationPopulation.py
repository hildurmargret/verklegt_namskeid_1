import csv

path='/Users/SaraLind/github/verklegt_namskeid_1/Documents/github/Verklegt1/UPDATEDSTUDENTDATA/'
skra1='Destinations.csv'
skra2 = 'pastFlights.csv'
skra3 = 'UpcomingFlights.csv'

file1 = path + skra1
file2 = path + skra2
file3 = path + skra3
Destination_array = []
pastFlights_array1 = []
pastFlights_array2 = []
PopularDest=[]

########### open file 1 ###########
with open(file1,'r') as csv_file:
    csv_reader1 = csv.DictReader(csv_file)
    for row in csv_reader1:
        if row['id'] != "KEF":
            Destination = row['id']
            Destination_array.append(Destination)
length = len(Destination_array)
print(length)
print(Destination_array)

########### open file 2 ###########
with open(file2,'r') as csv_file:
    csv_reader2 = csv.DictReader(csv_file)
    for row in csv_reader2:
        if row['departingFrom'] == 'KEF':
            pastFlights1 = row['arrivingAt']
            pastFlights_array1.append(pastFlights1)

for i in range(len(pastFlights_array1)):
    print(pastFlights_array1[i])


########### open file 3 ###########
with open(file3,'r') as csv_file:
    csv_reader3 = csv.DictReader(csv_file)
    for row in csv_reader3:
        if row['departingFrom'] == 'KEF':
            pastFlights2 = row['arrivingAt']
            pastFlights_array2.append(pastFlights2)

for i in range(len(pastFlights_array2)):
    print(pastFlights_array2[i])

########### Find the most popular destination ###########
PopularDest = Destination_array + pastFlights_array1 + pastFlights_array2
print("ME")
print(PopularDest)
