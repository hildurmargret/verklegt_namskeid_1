import csv

def list_all_aircraft():
    from leitaStaff import leitaStaff

    path='/Users/SaraLind/github/verklegt_namskeid_1/Documents/github/Verklegt1/UPDATEDSTUDENTDATA/'
    skra1='Aircraft.csv'
    skra2='AircraftType.csv'

    file1 = path + skra1
    file2 = path + skra2

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
