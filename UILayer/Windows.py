from UILayer.pagePrints import*
from LogicLayer.LL_API import*
from ModelClasses.Staff import*
from UILayer.addInp import*
from ModelClasses.Voyage import*
from LogicLayer.getStaff1_4 import*
from LogicLayer.getStaff5_6 import*
from LogicLayer.getStaff7_8 import*
from LogicLayer.leitaVoyage import*
from UILayer.printVoyageList import*
from LogicLayer.voyageByDate import*
from UILayer.printVoyagebyDates import*
from LogicLayer.voyageByWeek import*
from LogicLayer.getAircraft import*
from UILayer.UI_Manager import*
from UILayer.printWorkSchedule import*
from UILayer.printDestList import*
from DataLayer.saveWorkSchedule import*
from LogicLayer.allPilotsByLicence import*
from LogicLayer.searchPilotByLicence import*
from UILayer.printPilots import*
from LogicLayer.weeklyWorkSchedule import*


"""from Staff import*
from Voyage import*
from Destination import*
from Airplane import* """
"""
from getStaff1_4 import*
from OpenFile import*
from printList import*
from getPilotsByAirplanes import*
from getPilotByLicence import*
"""
from LogicLayer.listDestinationsAlphabetic import*
from LogicLayer.listDestinationPopularity import*

UI=UI_Manager()

class Windows():

    def updatePilot(self,print_):
        print_.window23()
        UI.UIupdatePilot()

    def updateCabin(self,print_):
        print_.window24()
        UI.UIupdateCabin()

    def updateStaff(self,print_):
        print_.window2()
        inp=int(input('Number: '))
        if inp==1:
            self.updatePilot(print_)
        elif inp==2:
            self.updateCabin(print_)

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
            input_string = input('Name or SSN: ')
            if input_string == 'CANCEL':
                self.getStaffInfo()
            else:
                linur=staffInfo(inp, input_string)
                for i in range(len(linur)):
                    print(linur[i].name)
        elif inp==5:
            print_.window12()
            input_string = input('Name or SSN: ')
            if input_string == 'CANCEL':
                self.getStaffInfo()
            else:
                numOfDest, pastFlights, upcFlights, employees = staffInfo2(inp, input_string)
                printDestList(numOfDest, pastFlights, employees)

        elif inp==6:
            print_.window12()
            input_string = input('Name or SSN: ')
            print_.window26()
            WC = input('Weekly or complete? ')
            if WC == str(1):
                print_.window19()
                week = input('Week: ')
                year = input('Year: ')
                flights, employees = weeklyWS(week, year, input_string)

            elif WC == str(2):
                numOfDest, pastFlights, upcFlights, employees = staffInfo2(input_string)

            print_.window13()
            input_save = input('Save? ')

            if WC == str(2):
                if input_save == str(1):
                    saveCompleteWS(pastFlights, employees)
                printCompleteWS(pastFlights, employees)
            elif WC==str(1):
                if input_save == str(1):
                    saveWeeklyWS(flights, employees,week,year)
                printWeeklyWS(flights,employees,week,year)

        elif inp==7:
            print_.window17()
            input_string = input('Date: ')
            emp, noemp = emplWorking(input_string)

            for i in range(len(noemp)):
                print(noemp[i].name)

        elif inp==8:
            print_.window17()
            input_string = input('Date: ')
            emp,noemp = emplWorking(input_string)

            for i in range(len(emp)):
                print(emp[i].name)

        else:
            linur=staffInfo(inp)

            for i in range(len(linur)):
                print(linur[i].name)

    def getAirplaneInfo(self,print_):
        print_.window14()
        inp=int(input("Number: "))
        if inp==1:
            UI.UIgettingAirplanes()
        elif inp==2:
            pilots, types = allPilotsByLicence()

            for i in range(len(pilots)):
                print(types[i])
                printPilotList(pilots[i])
                print('\n', end = '')

        elif inp==3:
            print_.window25()
            inpt = input('Airplane type: ')
            pilots = searchPilotsByLicence(inpt)
            printPilotList(pilots)


    def getVoyageInfo(self,print_):
        print_.window15()
        inp=int(input("number: "))
        if inp==1:
            print_.window16()
            input_string = input('Flight number: ')
            linur = leitaVoyage(input_string)
            printVoyageList(linur)

        elif inp==2:
            print_.window17()
            input_string = input('Date: ')
            dep, ret = voyageByDate(input_string)
            printVoyagebyDates(dep,ret)

        elif inp==3:
            print_.window19()
            input_week = input('Week number: ')
            input_year = input('Year: ')
            dep, ret = voyageByWeek(input_week, input_year)
            printVoyagebyDates(dep,ret)
        elif inp==0:
            self.getInformation(print_)

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
        print_.window9()
        add=Inp()
        [planeTypeId,manufacturer,airplaneModel,capacity,emptyWeight,maxTakeoffWeight,unitThrust,serviceCeiling,length,height,wingspan]=add.addAirplaneInp()
        airplane=createAirplane(planeTypeId,manufacturer,airplaneModel,capacity,emptyWeight,maxTakeoffWeight,unitThrust,serviceCeiling,length,height,wingspan)
        UI.UIsaveAircraft(airplane)


    def copyExistingVoyage(self,print_):
        print_.window6()


    def createNewVoyage(self,print_):
        print_.window7()
        add=Inp()
        [flightNumber,departingFrom,arrivingAt,departure,arrival,aircraftId,numberOfCabin,numberOfPilots]=add.addVoyageInp()
        voyage=createVoyage(flightNumber,departingFrom,arrivingAt,departure,arrival,aircraftId,numberOfCabin,numberOfPilots)
        UI.UIsaveVoyage(voyage)


    def createVoyages(self,print_):
        print_.window5()
        inp=int(input("number: "))
        if inp==1:
            self.copyExistingVoyage(print_)
        elif inp==2:
            self.createNewVoyage(print_)
        elif inp==0:
            self.create(print_)

    def createNewPilot(self,print_):
        print_.window3()
        add=Inp()
        [name,ssn,address,phoneNumber,mobileNumber,emailAddress,rank]=add.addStaffInp()
        airplaneLicense=input("Airplane Licence: ")
        ##add.addInp()
        pilot=createPilot(name,ssn,address,phoneNumber,mobileNumber,emailAddress,rank,airplaneLicense)
        UI.UIsavePilot(pilot)

    def createNewCabin(self,print_):
        print_.window4()
        add=Inp()
        [name,ssn,address,phoneNumber,mobileNumber,emailAddress,rank]=add.addStaffInp()
        cabin=createCabin(name,ssn,address,phoneNumber,mobileNumber,emailAddress,rank)
        UI.UIsaveCabin(cabin)

    def createNewStaff(self,print_):
        print_.window2()
        inp=int(input("number: "))
        if inp==1:
            self.createNewPilot(print_)
        elif inp==2:
            self.createNewCabin(print_)
        elif inp==0:
            self.create(print_)


    def createDestinations(self, print_):
        print_.window8()
        add = Inp()
        [country,distance,airport,contactName,contactNumber]=add.addDestinationInp()
        Dest=CreateDestination(country,distance,airport,contactName,contactNumber)
        UI.saveDestinationInFile(Dest)

    def create(self,print_):
        print_.window1() #Staff,voyage,destination,airplane
        inp=int(input("number: "))
        if inp==1:  #Staff valinn
            self.createNewStaff(print_)
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
