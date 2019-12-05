import csv
def pilotsByAirplanes():

    path='/Users/palinakroyer/github/verklegt_namskeid_1/Documents/github/Verklegt1/UPDATEDSTUDENTDATA/'
    skra='Crew.csv'
    file = path + skra
    dict={}
    with open(file,'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if row['role']=='Pilot':
                dict[row['licence']]=[]
    with open(file,'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            name=row['name']
            ssn=row['ssn']
        #    print(name)
            licence=row['licence']
        #    print(licence)

            for key in dict:
                if key==licence:
                    dict[key].append(name)
                    dict[key].append(ssn)


    print (dict)

    for key in dict:
        print(key)
        end=(len(dict[key]))
        for i in range(0,end,2):
            print(dict[key][i] + " " + dict[key][i+1])
        print("")
