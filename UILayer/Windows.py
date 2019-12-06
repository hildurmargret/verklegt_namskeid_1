from pagePrints import*
from Staff import*
from Voyage import*
from Destination import*
from Airplane import*
from getStaff1_4 import*
from OpenFile import*
from printList import*
from getAircraft import*
from getPilotsByAirplanes import*
from getPilotByLicence import*
from listDestinationsAlphabetic import*
from listDestinationPopulation import*


class Windows():

    def updateStaff(self,print_):
        pass


    def employeesToVoyage(self,print_):
        print_.window25()

    def updateInformation(self,print_):
        print_.window21()
        inp=int(input("number: "))
        if inp==1:
            self.updateStaff(print_)
        elif inp==2:
            print_.window22()
        elif inp==3:
            self.employeesToVoyage(print_)
        elif inp==0:
            self.mainMenu()



    def getStaffInfo(self,print_):
        print_.window11()
        inp=int(input("number: "))
        if inp==0:
            self.getInformation(print_)
        if inp==4:
            print_.window12()
            linur=staffInfo(inp)

            for i in range(len(linur)):
                for j in range(len(linur[0])-1):
                    print(toPrint[i][j] + ','),
                print(linur[i][j+1])
        else:
            linur=staffInfo(inp)
            for i in range(len(linur)):
                for j in range(len(linur[0])-1):
                    print(linur[i][j] + ','),
                print(linur[i][j+1])




    def getAirplaneInfo(self,print_):
        print_.window14()
        inp=int(input("number: "))
        if inp==1:
            list_all_aircraft()
        elif inp==2:
            pilotsByLicence()
        elif inp==3:
            pilotsByAirplanes()

    def getVoyageInfo(self,print_):
        print_.window15()

    def getVoyageInfoWeek(self,print_):
        print_.window19()

    def getDestinationsInfo(self,print_):
        print_.window20()
        inp=int(input("number: "))
        if inp==1:
            listAllDestinationsAlph()
        elif inp==2:
            MostPopularDestination()
        elif inp ==0:
            self.mainMenu() #LAGA!!

    def getInformation(self,print_):
        print_.window10() #Staff,airplanes,voyage,destinations
        inp=int(input("number: "))
        if inp==1:
            self.getStaffInfo(print_)
        elif inp==2:
            self.getAirplaneInfo(print_)
        elif inp==3:
            self.getVoyageInfo(print_)
        elif inp==4:
            self.getDestinationsInfo(print_)
        elif inp==0:
            self.mainMenu()



    def createAirplanes(self,print_):
        new_airplane=Airplane()
        print_.window9()
        new_airplane.addInfo()  #insert new airplane


    def createDestinations(self,print_):
        new_dest=Destination()
        print_.window8()
        new_dest.addInfo()

    def copyExistingVoyage(self,print_):
        print_.window6()


    def createNewVoyage(self,print_):
        new_voyage=Voyage()
        print_.window7() #Voyage; info
        new_voyage.addInfo()


    def createVoyages(self,print_):
        print_.window5()
        inp=int(input("number: "))
        if inp==1:
            self.copyExistingVoyage(print_)
        elif inp==2:
            self.createNewVoyage(print_)
        elif inp==0:
            self.create(print_)


    def flightAttendant(self,print_):
        new_staff=Cabin()
        print_.window4() #Pilot,flight attendant; info
        new_staff.addInfo()

    def pilot(self,print_):
        new_pilot=Pilot()
        print_.window3() #Adding new pilot; info
        new_pilot.addInfo()


    def createStaff(self,print_):
        print_.window2()
        inp=int(input("number: "))
        if inp==1:
            self.pilot(print_)
        elif inp==2:
            self.flightAttendant(print_)
        elif inp==0:
            self.create(print_)


    def create(self,print_):
        print_.window1() #Staff,voyage,destination,airplane
        inp=int(input("number: "))
        if inp==1:  #Staff valinn
            self.createStaff(print_)
        elif inp==2:
            self.createVoyages(print_)
        elif inp==3:
            self.createDestinations(print_)
        elif inp==4:
            self.createAirplanes(print_)
        elif inp==0:
            self.mainMenu()


    def mainMenu(self):
        print_=pagePrints(100,40)
        print_.frontPage() #'c', 'g', 'u'
        inp=input()
        if inp=="c":
            self.create(print_)
        elif inp=='g':  #Get information
            self.getInformation(print_) #Staff,airplanes,voyage,destinations
        elif inp=='u':
            self.updateInformation(print_)
