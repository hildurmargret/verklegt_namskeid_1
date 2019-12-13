import csv
from LogicLayer.leitaStaff import *
from ModelClasses.Staff import *
from DataLayer.OpenFile import *
from DataLayer.read_crew_file import *

def staffInfo(input_num, input_string):

    skra='CrewCopy.csv'

    file_=OpenFile(skra)
    allStaff=read_crew_file(file_) #klasa tilvik af ollum staff i lista

    #tomur listi til að nota
    employees = []

    #fer i gegnum alla starfsmenn
    for i in range(len(allStaff)):
        if input_num==1: #ef input er 1 set eg alla starfsmenn i lista
            empl = createStaff(allStaff[i].name, allStaff[i].SSN, allStaff[i].address, allStaff[i].phoneNumber,allStaff[i].emailAddress,allStaff[i].rank,allStaff[i].role,allStaff[i].licence)
            employees.append(empl)

        elif input_num==2: #ef input er 2 finn eg starfsmenn með role pilot og set i lista
            if allStaff[i].role=='Pilot':
                empl = createStaff(allStaff[i].name, allStaff[i].SSN, allStaff[i].address, allStaff[i].phoneNumber,allStaff[i].emailAddress,allStaff[i].rank,allStaff[i].role,allStaff[i].licence)
                employees.append(empl)

        elif input_num==3: #ef input er 3 finn eg starfsmenn með role cabincrew og set i lista
            if allStaff[i].role=='Cabincrew':
                 empl = createStaff(allStaff[i].name, allStaff[i].SSN, allStaff[i].address, allStaff[i].phoneNumber,allStaff[i].emailAddress,allStaff[i].rank,allStaff[i].role,allStaff[i].licence)
                 employees.append(empl)

        elif input_num==4: #þarf að leita eftir starfsmanni eftir ssn eða name, nota leitaStaff fallið til þess, það skilar listum af kennitölum og rank sem passa við inputið (leitarorðið)
            ssn, rank = leitaStaff(input_string, allStaff)

            if ssn==0 and rank == 0: #ef eg fann engan sem passaði skila eg 0
                return 0
            else:
                for j in range(len(ssn)): #annars finn ég alla starfsmenn i allStaff lista sem passa við ssn og set i employees listann
                    if allStaff[i].SSN == ssn[j]:
                        empl = createStaff(allStaff[i].name, allStaff[i].SSN, allStaff[i].address, allStaff[i].phoneNumber,allStaff[i].emailAddress,allStaff[i].rank,allStaff[i].role,allStaff[i].licence)
                        employees.append(empl)
    #skila listanum
    return employees
