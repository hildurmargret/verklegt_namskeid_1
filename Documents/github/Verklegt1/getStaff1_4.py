
def staffInfo(inp):

    import csv
    from leitaStaff import leitaStaff

    path='/Users/hildur/Documents/github/verklegt_namskeid_1/Documents/github/Verklegt1/UPDATEDSTUDENTDATA/'
    skra='Crew.csv'

    #inp=2
    inpt='3003962187'

    file=path+skra

    ssn='yellow'
    rank=''
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
                #print(row['ssn'])
                if row['ssn']==ssn:
                    lina=row['ssn']+','+row['name']+','+row['role']+','+row['rank']+','+row['licence']
                    arr = lina.split(',')
                    lines.append(arr)
                    break
                #break
    #print(lines)
    return lines
