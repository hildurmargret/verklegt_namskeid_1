
def leitaStaff(inpt, file, ssn, rank):

    import csv

    with open(file,'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if inpt.isdigit():
                if inpt in row['ssn']:
                    if row['licence']!='N/A':
                        #print(row['ssn'], row['name'], row['role'], row['rank'], row['licence'])
                        ssn=row['ssn']
                        rank=row['rank']

                        return ssn, rank
                    else:
                        #print(row['ssn'], row['name'], row['role'], row['rank'])
                        ssn=row['ssn']
                        rank=row['rank']

                        return ssn, rank
            else:
                if inpt in row['name']:
                    if row['licence']!='N/A':
                        #print(row['ssn'], row['name'], row['role'], row['rank'], row['licence'])
                        ssn=row['ssn']
                        rank=row['rank']

                        return ssn, rank
                    else:
                        #print(row['ssn'], row['name'], row['role'], row['rank'])
                        ssn=row['ssn']
                        rank=row['rank']

                        return ssn, rank
