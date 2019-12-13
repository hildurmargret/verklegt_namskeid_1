

def leitaStaff(inpt, allStaff):
    ssn=[]
    rank=[]

    empl_found = 0

    for i in range(len(allStaff)): #fer gegnum alla starfsmenn
        if inpt.isdigit(): #ef notandi sláði inn kennitölu
            if inpt in allStaff[i].SSN: #ef ég finn input notanda í SSN þá:
                ssn.append(allStaff[i].SSN) #set ég kennitöluna í ssn listann
                rank.append(allStaff[i].rank) #set líka rank í rank lista
                empl_found=1
        else: #geri það sama hér nema notandi hefur hér slegið inn nafn og leita því í name
            if inpt.lower() in allStaff[i].name.lower():
                ssn.append(allStaff[i].SSN)
                rank.append(allStaff[i].rank)
                empl_found=1
    #skila 0 ef eg fann ekkert
    if empl_found == 0:
        return 0,0
    else:
        return ssn, rank
