
def staffInfo(inp):

    import csv
    from leitaStaff import leitaStaff

    path='/Users/hildur/Documents/github/verklegt_namskeid_1/Documents/github/Verklegt1/UPDATEDSTUDENTDATA/'
    skra='Crew.csv'

    inpt='son'

    file=path+skra

    ssn=[]
    rank=[]
    employees = {'ssn':[], 'name':[], 'role':[], 'rank':[], 'licence':[], 'address':[], 'phonenumber':[]}

    with open(file,'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if inp==1:
                employees['ssn'].append(row['ssn'])
                employees['name'].append(row['name'])
                employees['role'].append(row['role'])
                employees['rank'].append(row['rank'])
                employees['licence'].append(row['licence'])
                employees['address'].append(row['address'])
                employees['phonenumber'].append(row['phonenumber'])

            elif inp==2:
                if row['role']=='Pilot':
                    employees['ssn'].append(row['ssn'])
                    employees['name'].append(row['name'])
                    employees['role'].append(row['role'])
                    employees['rank'].append(row['rank'])
                    employees['licence'].append(row['licence'])
                    employees['address'].append(row['address'])
                    employees['phonenumber'].append(row['phonenumber'])

            elif inp==3:
                if row['role']=='Cabincrew':
                    employees['ssn'].append(row['ssn'])
                    employees['name'].append(row['name'])
                    employees['role'].append(row['role'])
                    employees['rank'].append(row['rank'])
                    employees['licence'].append(row['licence'])
                    employees['address'].append(row['address'])
                    employees['phonenumber'].append(row['phonenumber'])

            elif inp==4:
                #inpt=input('Please enter the name or SSN of employee')
                ssn,rank=leitaStaff(inpt,file,ssn,rank)
                for i in range(len(ssn)):
                    if row['ssn']==ssn[i]:
                        employees['ssn'].append(row['ssn'])
                        employees['name'].append(row['name'])
                        employees['role'].append(row['role'])
                        employees['rank'].append(row['rank'])
                        employees['licence'].append(row['licence'])
                        employees['address'].append(row['address'])
                        employees['phonenumber'].append(row['phonenumber'])

                        break
    return employees

empl = staffInfo(4)

#end=len(empl['name'])

#for i in range(0,end):
#    for key in empl:
#        print(empl[key][i])
#    print
