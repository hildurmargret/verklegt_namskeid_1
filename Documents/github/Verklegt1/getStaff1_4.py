
def staffInfo(inp):

    import csv
    from leitaStaff import leitaStaff

    path='/Users/valdisbaerings/Documents/verklegt_namskeid_1/Documents/github/Verklegt1/UPDATEDSTUDENTDATA/'
    skra='Crew.csv'

    #inp=2
    inpt='son'

    file=path+skra

    ssn=['ssn']
    rank=['rank']
    lines = []

    with open(file,'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if inp==1:
                lina=row['ssn']+','+row['name']+','+row['role']+','+row['rank']+','+row['licence']
                arr = lina.split(',')
                lines.append(arr)
                #print(lines)
            elif inp==2:
                if row['role']=='Pilot':
                    lina=row['ssn']+','+row['name']+','+row['role']+','+row['rank']+','+row['licence']
                    arr = lina.split(',')
                    lines.append(arr)
                    #print(row['ssn'], row['name'], row['role'], row['rank'], row['licence'])
            elif inp==3:
                if row['role']=='Cabincrew':
                    lina=row['ssn']+','+row['name']+','+row['role']+','+row['rank']
                    arr = lina.split(',')
                    lines.append(arr)
                    #print(row['ssn'], row['name'], row['role'], row['rank'])
            elif inp==4:
                #inpt=input('Please enter the name or SSN of employee')
                ssn,rank=leitaStaff(inpt,file,ssn,rank)
                for i in range(len(ssn)):
                    if row['ssn']==ssn[i]:
                        lina=row['ssn']+','+row['name']+','+row['role']+','+row['rank']+','+row['licence']
                        arr = lina.split(',')
                        lines.append(arr)
                        break
    return lines
