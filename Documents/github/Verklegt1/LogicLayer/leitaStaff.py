
def leitaStaff(inpt, file, ssn, rank):

    import csv
    with open(file,'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            if inpt.isdigit():
                if inpt in row['ssn']:
                        #print(row['ssn'], row['name'], row['role'], row['rank'], row['licence'])
                    ssn.append(row['ssn'])
                    rank.append(row['rank'])

            else:
                #print(inpt)
                #print(row['ssn'])
                if inpt in row['name']:
                        #print(row['ssn'], row['name'], row['role'], row['rank'], row['licence'])
                    #ssn=row['ssn']
                    #rank=row['rank']
                    ssn.append(row['ssn'])
                    rank.append(row['rank'])
                    #for i in range(len(ssn)):
                    #    print(ssn[i])
        return ssn, rank
