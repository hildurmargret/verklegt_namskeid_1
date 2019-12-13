import csv
from LogicLayer.leitaStaff import *
from ModelClasses.Staff import *
from DataLayer.OpenFile import *
from DataLayer.read_crew_file import *

def staffInfo(input_num, input_string):

    skra='Crew.csv'

    file_=OpenFile(skra)
    allStaff=read_crew_file(file_)

    ssn=[]
    rank=[]
    employees = []

    for i in range(len(allStaff)):
        if input_num==1:
            empl = createStaff(allStaff[i].name, allStaff[i].SSN, allStaff[i].address, allStaff[i].phoneNumber,allStaff[i].emailAddress,allStaff[i].rank,allStaff[i].role,allStaff[i].licence)
            employees.append(empl)

        elif input_num==2:
            if allStaff[i].role=='Pilot':
                empl = createStaff(allStaff[i].name, allStaff[i].SSN, allStaff[i].address, allStaff[i].phoneNumber,allStaff[i].emailAddress,allStaff[i].rank,allStaff[i].role,allStaff[i].licence)
                employees.append(empl)

        elif input_num==3:
            if allStaff[i].role=='Cabincrew':
                 empl = createStaff(allStaff[i].name, allStaff[i].SSN, allStaff[i].address, allStaff[i].phoneNumber,allStaff[i].emailAddress,allStaff[i].rank,allStaff[i].role,allStaff[i].licence)
                 employees.append(empl)

        elif input_num==4:
            ssn, rank = leitaStaff(input_string, allStaff, ssn, rank)

            if ssn==0 and rank == 0:
                return 0
            else:
                for j in range(len(ssn)):
                    if allStaff[i].SSN == ssn[j]:
                        empl = createStaff(allStaff[i].name, allStaff[i].SSN, allStaff[i].address, allStaff[i].phoneNumber,allStaff[i].emailAddress,allStaff[i].rank,allStaff[i].role,allStaff[i].licence)
                        employees.append(empl)
                        break

    return employees
