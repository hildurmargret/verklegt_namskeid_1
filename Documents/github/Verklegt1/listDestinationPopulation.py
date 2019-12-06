from OpenFile import*

def MostPopularDestination():

    Destination_array = []
    pastFlights_array1 = []
    pastFlights_array2 = []
    PopularDest=[]

    ########### open file 1 ###########
    file1 = OpenFile('Destinations.csv')
    with file1 as csv_file:
        csv_reader1 = csv.DictReader(csv_file)
        for row in csv_reader1:
            if row['id'] != "KEF":
                Destination = row['id']
                Destination_array.append(Destination)
    length = len(Destination_array)


    ########### open file 2 ###########
    file2 = OpenFile('pastFlights.csv')
    with file2 as csv_file:
        csv_reader2 = csv.DictReader(csv_file)
        for row in csv_reader2:
            if row['departingFrom'] == 'KEF':
                pastFlights1 = row['arrivingAt']
                pastFlights_array1.append(pastFlights1)


    ########### open file 3 ###########
    file3 = OpenFile('UpcomingFlights.csv')
    with file3 as csv_file:
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

MostPopularDestination()
