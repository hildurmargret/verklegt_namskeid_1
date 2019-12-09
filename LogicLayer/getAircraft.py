import csv

def list_all_aircraft():


    path="/Users/palinakroyer/github/verklegt_namskeid_1/"
    skra1='Aircraft.csv'
    skra2='AircraftType.csv'
    skra3='Crew.csv'

    file1 = path + skra1
    file2 = path + skra2
    file3 = path + skra3

    line1 = []
    line2 = []
    dict={}

    with open(file1,'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            dict[row['planeInsignia']]=[row['planeTypeId']]


    with open(file2,'r') as csv_file:
        csv_reader2 = csv.DictReader(csv_file)
        for row in csv_reader2:
            capacity = row['capacity']
            planetype= row['planeTypeId']
            for key in dict:
                if dict[key][0]==planetype:
                    dict[key].append(capacity)


    for key in dict:
        print(key+": "+dict[key][0]+", "+dict[key][1])
