import csv
path="/Users/palinakroyer/github/verklegt_namskeid_1/Documents/github/Verklegt1/UPDATEDSTUDENTDATA/"
skra1="UpcomingFlights copy2.csv"
skra2="Crew.csv"
file1=path+skra1
file2=path+skra2
fDEST=open(file1, "a")
fCREW=open(file2, "a")
dict={}
inp="3009907461"
flNo = 'NA021'
with open(file2,'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        if (inp==row['ssn']):
            role=row['role']
            rank=row['rank']

with open(file1,'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    print(csv_reader)

    with open(file1, 'w') as new_file:
        fieldnames=['flightNumber','departingFrom','arrivingAt','departure','arrival','captain','copilot','fsm','fa1','fa2']
        csv_writer=csv.DictWriter(new_file, fieldnames=fieldnames)

        for line in csv_reader:
            print(line)
            if flNo == line['flightNumber']:

                if rank=='Captain':
                    #csv_writer.writeheader()
                    #if not row['Captain']:
                #    dict[row['captain']]=inp

                    csv_writer.writerow({'flightNumber':flNo,'departingFrom':'halo','arrivingAt':'halo','departure':'halo','arrival':'halo','captain': 'halo','copilot':'halo','fsm':'halo','fa1':'halo','fa2':'halo'})
                    #else:
                    #    print("The voyage already has a captain")
                """if rank=='Copilot':
                    if not row['copilot']:
                        fDEST.write(inp)
                    else:
                        print("The voyage already has a copilot")
                if rank=='Flight Service Manager':
                    if not row['fsm']:
                        fDEST.write(inp)
                    else:
                        print("The voyage already has a flight service manager")
                if rank=='Flight Attendant':
                    if not row['fa1']:
                        fDEST.write(inp)
                    elif not row['fa2']:
                        fDEST.write(inp)
                    else:
                        print('The voyage already has two flight attendant')"""
