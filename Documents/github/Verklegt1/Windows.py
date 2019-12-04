from pagePrints import*
from Staff import*
from Voyage import*
from Destination import*
from Airplane import*


class Windows():

    def updateStaff(self,print_):
        print_.window12()

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



    def staffInfo(self,print_):
        print_.window11()
        inp=int(input("number: "))
        if inp==4:
            print_.window12()
        elif inp==5:
            print_.window12()
        elif inp==6:
            print_.window12()
            print_.window13()
        elif inp==0:
            self.getInformation(print_)


    def airplaneInfo(self,print_):
        print_.window14()

    def voyageInfo(self,print_):
        print_.window15()

    def voyageInfoWeek(self,print_):
        print_.window19()

    def destinationsInfo(self,print_):
        print_.window20()

    def getInformation(self,print_):
        print_.window10() #Staff,airplanes,voyage,destinations
        inp=int(input("number: "))
        if inp==1:
            self.staffInfo(print_)
        elif inp==2:
            self.airplaneInfo(print_)
        elif inp==3:
            self.voyageInfo(print_)
        elif inp==4:
            self.destinationsInfo(print_)
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
        new_staff=Staff()
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
