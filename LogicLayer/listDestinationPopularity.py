import csv
#from DataLayer.OpenFile import*

def MostPopularDestination():

    Destination_array = []
    pastFlights_array1 = []
    pastFlights_array2 = []
    PopularDest=[]

    path='/Users/SaraLind/github/verklegt_namskeid_1/csvFiles/'

    ########### open file 1 ###########
    skra1 = 'Destinations.csv'
    file1 = path+skra1
    #file1 = OpenFile(skra1)
    with open(file1,'r') as csv_file:
        csv_reader1 = csv.DictReader(csv_file)
        for row in csv_reader1:
            if row['id'] != "KEF":
                Destination = row['id']
                Destination_array.append(Destination)
    length = len(Destination_array)


    ########### open file 2 ###########
    skra2 = 'pastFlights.csv'
    file2 = path+skra2
    with open(file2,'r') as csv_file:
        csv_reader2 = csv.DictReader(csv_file)
        for row in csv_reader2:
            if row['departingFrom'] == 'KEF':
                pastFlights1 = row['arrivingAt']
                pastFlights_array1.append(pastFlights1)


    ########### open file 3 ###########
    skra3 = 'pastFlights.csv'
    file3 = path + skra3
    with open(file3, 'r') as csv_file:
        csv_reader3 = csv.DictReader(csv_file)
        for row in csv_reader3:
            if row['departingFrom'] == 'KEF':
                pastFlights2 = row['arrivingAt']
                pastFlights_array2.append(pastFlights2)


    ########### Find the most popular destination ###########
    PopularDest =pastFlights_array1 + pastFlights_array2

    counter = []
    largest=0
    TheCounter=0
    count=0

    for i in range(length):
        counter.append(0)


    for i in range(length-1):
        for j in range(len(PopularDest)):
            if Destination_array[i] == PopularDest[j]:
                counter[i] +=1
    #Find the largest value
    for i in range(length-1):
        if counter[i] > largest:
            largest = counter[i]

    #Find the location of biggest value
    for i in range(length-1):
        if counter[i] == largest:
            count = TheCounter
        TheCounter += 1

    #Find the most popular destination
    mostPopular = Destination_array[count]
    print("Most popular destination is: ", mostPopular)
    return mostPopular
