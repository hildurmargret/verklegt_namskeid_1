

def leitaStaff(inpt, allStaff, ssn, rank):

    updssn=[]

    for i in range(len(allStaff)):
        if inpt.isdigit():
            if inpt in allStaff[i].SSN:
                ssn.append(allStaff[i].SSN)
                rank.append(allStaff[i].rank)
        else:
            if inpt in allStaff[i].name:
                #print(allStaff[i].name)
                ssn.append(allStaff[i].SSN)
                rank.append(allStaff[i].rank)

    #with open(file,'r') as csv_file:
    # with file_ as csv_file:
    #     csv_reader = csv.DictReader(csv_file)
    #
    #     for row in csv_reader:
    #         if inpt.isdigit():
    #             if inpt in row['ssn']:
    #                 ssn.append(row['ssn'])
    #                 rank.append(row['rank'])
    #
    #         else:
    #             if inpt in row['name']:
    #                 ssn.append(row['ssn'])
    #                 rank.append(row['rank'])
    for i in ssn:
        if i not in updssn:
            updssn.append(i)
    
    return updssn, rank
