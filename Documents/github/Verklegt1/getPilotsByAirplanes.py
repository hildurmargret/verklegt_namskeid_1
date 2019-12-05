import csv
def pilotsByAirplanes():

    path='/Users/palinakroyer/github/verklegt_namskeid_1/Documents/github/Verklegt1/UPDATEDSTUDENTDATA/'
    skra='Crew.csv'
    file = path + skra
    dict={}
    with open(file,'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            dict[row['licence']]=[]
    with open(file,'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            name=row['name']
        #    print(name)
            licence=row['licence']
        #    print(licence)

            for key in dict:
                if key==licence:
                    dict[key].append(name)


    for key in dict:
        for value in key:
            print(key+": "+dict[key][value])
