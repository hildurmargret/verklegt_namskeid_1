

def leitaStaff(inpt, allStaff, ssn, rank):

    updssn=[]

    for i in range(len(allStaff)): #fer gegnum alla starfsmenn
        if inpt.isdigit(): #ef notandi sláði inn kennitölu
            if inpt in allStaff[i].SSN: #ef ég finn input notanda í SSN þá:
                ssn.append(allStaff[i].SSN) #set ég kennitöluna í ssn listann
                rank.append(allStaff[i].rank) #set líka rank í rank lista
        else: #geri það sama hér nema notandi hefur hér slegið inn nafn og leita því í name
            if inpt in allStaff[i].name:
                ssn.append(allStaff[i].SSN)
                rank.append(allStaff[i].rank)

    #passa að tvítelja ekki kennitölur
    # for i in ssn:
    #     if i not in updssn:
    #         updssn.append(i)

    return ssn, rank
