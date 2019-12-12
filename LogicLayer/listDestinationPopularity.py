import csv
from DataLayer.OpenFile import*
from DataLayer.getDestinations import*
from DataLayer.read_pastFlights import *

def MostPopularDestination():

    dest_arr = []
    pastFlights_array = []
    upcFlights_array = []
    PopularDest=[]

    #path='/Users/SaraLind/github/verklegt_namskeid_1/csvFiles/'

    ########### open file 1 ###########
    skra1 = 'DestinationsCopy.csv'
    file1 = OpenFile(skra1)
    allDest = getDestinations()

    for i in range(len(allDest)):
        if allDest[i].id != 'KEF':
            Destination=allDest[i].id
            dest_arr.append(Destination)
    length=len(dest_arr)


    # with file1 as csv_file:
    #     csv_reader1 = csv.DictReader(csv_file)
    #     for row in csv_reader1:
    #         if row['id'] != "KEF":
    #             Destination = row['id']
    #             Destination_array.append(Destination)
    # length = len(Destination_array)
    #

    ########### open file 2 ###########
    skra2 = 'PastFlights copy.csv'
    #file2 = OpenFile(skra2)

    allPastFlights=read_pastFlights(skra2)

    for i in range(len(allPastFlights)):
        if allPastFlights[i].departingFrom == 'KEF':
            pastFlights = allPastFlights[i].arrivingAt
            pastFlights_array.append(pastFlights)

    # with file2 as csv_file:
    #     csv_reader2 = csv.DictReader(csv_file)
    #     for row in csv_reader2:
    #         if row['departingFrom'] == 'KEF':
    #             pastFlights1 = row['arrivingAt']
    #             pastFlights_array1.append(pastFlights1)


    ########### open file 3 ###########
    skra3 = 'UpcomingFlights copy3.csv'
    #file3 = OpenFile(skra3)

    allUPcFlights=read_pastFlights(skra3)

    for i in range(len(allUPcFlights)):
        if allUPcFlights[i].departingFrom == 'KEF':
            upcFlights = allUPcFlights[i].arrivingAt
            upcFlights_array.append(upcFlights)

    # with file3 as csv_file:
    #     csv_reader3 = csv.DictReader(csv_file)
    #     for row in csv_reader3:
    #         if row['departingFrom'] == 'KEF':
    #             pastFlights2 = row['arrivingAt']
    #             pastFlights_array2.append(pastFlights2)


    ########### Find the most popular destination ###########
    PopularDest =pastFlights_array + upcFlights_array

    counter = []
    largest=0
    TheCounter=0
    count=0

    for i in range(length):
        counter.append(0)


    for i in range(length-1):
        for j in range(len(PopularDest)):
            if dest_arr[i] == PopularDest[j]:
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
    mostPopular = dest_arr[count]

    return mostPopular
