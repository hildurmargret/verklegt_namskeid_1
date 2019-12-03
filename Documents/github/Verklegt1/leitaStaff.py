
def leitaStaff(inpt, file):

    import csv
    emp=''

    with open(file,'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if inpt.isdigit():
                if inpt in row['ssn']:
                    if row['licence']!='N/A':
                    #emp=row
                        print(row['ssn'], row['name'], row['role'], row['rank'], row['licence'])
                    else:
                        emp=row
                        print(row[ssn], row['name'], row['role'], row['rank'])
            else:
                if inpt in row['name']:
                    if row['licence']!='N/A':
                    #emp=row
                        print(row['ssn'], row['name'], row['role'], row['rank'], row['licence'])
                    else:
                        #emp=row
                        print(row['ssn'], row['name'], row['role'], row['rank'])
