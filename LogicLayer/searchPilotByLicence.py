
import csv
from ModelClasses.Staff import*
from DataLayer.OpenFile import *
from DataLayer.read_crew_file import *
def searchPilotsByLicence(airplaneType):

    #tek inn typu flugvelar
    file1='CrewCopy.csv'
    file_=OpenFile(file1)
    allStaff=read_crew_file(file_)

    pilots = []
    #fer i gegnum alla starfsmenn og tekka hverjir passa við flugvelatypuna og by til starfsmanna klasatilvik og set i lista til að skila ut
    for i in range(len(allStaff)):
        if allStaff[i].role == 'Pilot' and allStaff[i].licence==airplaneType:
            emp = createStaff(allStaff[i].name, allStaff[i].SSN, allStaff[i].address, allStaff[i].phoneNumber,allStaff[i].emailAddress,allStaff[i].rank,allStaff[i].role,allStaff[i].licence)
            pilots.append(emp)

    return pilots
