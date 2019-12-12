from UILayer.pagePrints import*
from LogicLayer.LL_API import*
from ModelClasses.Staff import*
from UILayer.addInp1 import*
from UILayer.addInp2 import*
from UILayer.addInp3 import*
from UILayer.addInp4 import*
from ModelClasses.Voyage import*
from LogicLayer.getStaff1_4nytt import*
from LogicLayer.getStaff5nytt import*
from LogicLayer.getStaff7_8nytt import*
from LogicLayer.leitaVoyage import*
from UILayer.printVoyageList import*
from LogicLayer.voyageByDate import*
from UILayer.printVoyagebyDates import*
from LogicLayer.voyageByWeek import*
from DataLayer.getAircraft import*
from UILayer.UI_Manager import*
from UILayer.printWorkSchedule import*
from UILayer.printDestList import*
from DataLayer.saveWorkSchedule import*
from LogicLayer.allPilotsByLicence import*
from LogicLayer.searchPilotByLicence import*
from UILayer.printPilots import*
from LogicLayer.weeklyWorkSchedule import*
from DataLayer.getDestinations import*
from LogicLayer.listDestinationPopularity import*
from UILayer.chooseEmplFromList import*
from DataLayer.getAllPlaneTypes import*
from DataLayer.getAllPlaneTypes import*
from LogicLayer.fixFlightNumbers import*
from DataLayer.saveUpdatedFlights import*
from LogicLayer.airplaneInUse import*
from UILayer.printAirplaneStatus import*
from LogicLayer.voyageStatus import*
from UILayer.printVoyageStatus import*
from UILayer.printSearchedVoyage import*
from UILayer.printAirplaneStatus import*
from LogicLayer.voyageStatus import*
from UILayer.printVoyageStatus import*
from UILayer.chooseVoyageFromList import*
from LogicLayer.mostPOPinfo import*


UI=UI_Manager()

class Windows():

    def aircraftToVoyage(self,print_):
        UI.UIaircraftToVoyage()




    def updateVoyage(self,print_):
        print_.window7()
        UI.UIupdateVoyage()

    def updatePilot(self,print_):
        print_.window23()
        UI.UIupdateStaff()

    def updateCabin(self,print_):
        print_.window24()
        UI.UIupdateStaff()

    def updateStaff(self,print_):
        print_.window2()
        inp=int(input('Number: '))
        if inp==1:
            self.updatePilot(print_)
        elif inp==2:
            self.updateCabin(print_)

    def employeesToVoyage(self,print_):
        UI.UIemployeesToVoyage()
        print_.window25()
        add=Inp3()
        voyage=createFlightRoute()
        #voyage=add.addVoyageInp(voyage)


    def updateInformation(self,print_):
        print_.window21()
        inp=int(input("number: "))
        if inp==1:
            self.updateStaff(print_)
        elif inp==2:
            print_.window22()
            update=updateDestInput()
            dest=UI.UIupdateDestination()
            dest=DestinationFromList(dest)
            dest=update.addDestInp(dest)

            if dest == 0:
                self.mainMenu(print_)
            else:
                UI.UIsaveNewDestination(dest)
        elif inp==3:
            self.employeesToVoyage(print_)
        elif inp==4:
            self.updateVoyage(print_)
        elif inp==5:
            self.aircraftToVoyage(print_)
        elif inp==0:
            self.mainMenu()




    def getStaffInfo(self,print_):
        print_.window11()
        inp=int(input("Number: "))
        if inp==0:
            self.getInformation(print_)
        if inp==4:
            print_.window12()
            input_string = input('Name or SSN: ')
            if input_string == 'CANCEL':
                self.getStaffInfo(print_)
            else:
                linur=staffInfo(inp, input_string)
                for i in range(len(linur)):
                    print(linur[i].name)
        elif inp==5:
            print_.window12()
            input_string = input('Name or SSN: ')
            if input_string == 'CANCEL':
                self.getStaffInfo(print_)
            else:
                employees = staffInfo(4, input_string)
                employee = emplFromList(employees)
                numOfDest, pastFlights, upcFlights, empl = staffInfo2(employee.SSN)
                printDestList(numOfDest, pastFlights, empl)

        elif inp==6:
            print_.window12()
            input_string = input('Name or SSN: ')
            employees = staffInfo(4, input_string)
            employee = emplFromList(employees)
            print_.window26()
            WC = input('Weekly or complete? ')
            if WC == str(1):
                print_.window19()
                week = input('Week: ')
                year = input('Year: ')
                flights, empl = weeklyWS(week, year, employee.SSN)
                print(flights)

            elif WC == str(2):
                numOfDest, pastFlights, upcFlights, empl = staffInfo2(employee.SSN)
            print_.window13()
            input_save = input('Save? ')

            if WC == str(2):
                if input_save == str(1):
                    saveCompleteWS(pastFlights, upcFlights, empl)
                printCompleteWS(pastFlights, upcFlights, empl)
            elif WC==str(1):
                if input_save == str(1):
                    saveWeeklyWS(flights, empl,week,year)
                printWeeklyWS(flights,empl,week,year)

        elif inp==7:
            print_.window17()
            input_string = input('Date: ')
            emp, noemp, dest = emplWorking(input_string)

            for i in range(len(noemp)):
                print(noemp[i].name)

        elif inp==8:
            print_.window17()
            input_string = input('Date: ')
            emp, noemp, dest = emplWorking(input_string)

            for i in range(len(dest)):
                print(dest[i])

        else:
            linur=staffInfo(inp,'')

            for i in range(len(linur)):
                print(linur[i].name)


    def getAirplaneInfo(self,print_):
        print_.window14()
        inp=int(input("Number: "))
        if inp==1:
            UI.UIgettingAirplanes()
        elif inp==2:
            pilots = allPilotsByLicence()
            types = getAllTypes()

            for i in range(len(pilots)):
                print(types[i])
                printPilotList(pilots[i])
                print('\n', end = '')

        elif inp==3:
            print_.window25()
            inpt = input('Airplane type: ')
            pilots = searchPilotsByLicence(inpt)
            printPilotList(pilots)
        elif inp==4:
            print_.window17()
            input_date=input('Date: ')
            print_.window29()
            input_time=input('Time: ')
            inAir, onGround=airplaneInUse(input_date, input_time)
            printAirplaneStatus(inAir, onGround, input_date, input_time)


    def getVoyageInfo(self,print_):
        print_.window15()
        inp=int(input("number: "))
        if inp==1:
            voyage = []
            print_.window16()
            input_string = input('Flight number: ')
            voyage.extend(UI.UIgettingVoyage(input_string))
            printSearchedVoyage(voyage)

        elif inp==2:
            print_.window17()
            input_string = input('Date: ')
            dep, ret = voyageByDate(input_string)
            printVoyagebyDates(dep,ret)

        elif inp==3:
            print_.window19()
            input_week = input('Week number: ')
            input_year = input('Year: ')
            voyages, daterange = voyageByWeek(input_week, input_year)
            printVoyageList(voyages, daterange)
            #printVoyagebyDates(dep,ret)

        elif inp==4:
            print_.window17()
            input_date=input('Date: ')
            print_.window29()
            input_time=input('Time: ')
            dep, ret =voyageByDate(input_date)
            status = voyageStatus(dep, ret, input_date, input_time)
            printVoyageStatus(dep, ret, status,input_date, input_time)

        elif inp==0:
            self.getInformation(print_)

    def getVoyageInfoWeek(self,print_):
        print_.window19()


    def getDestinationsInfo(self,print_):
        print_.window20()
        inp=int(input("number: "))
        if inp==1:
            listOfDest=getDestinations()
            for i in range(len(listOfDest)):
                print(listOfDest[i].destination)

        elif inp==2:
            mostpop=MostPopularDestination()
            destList=getDestinations()
            popInfo=mostPOPinfo(mostpop,destList)

            print('The most popular destination is: ',popInfo.destination.upper())
            print('Airport: ' + popInfo.id + '\n'+ 'Country: '+ popInfo.country + '\n'+ 'Distance from Iceland: '+ popInfo.distance + '\n'+ 'Destination contact: '+ popInfo.contactName + ' - tel: ' + popInfo.contactNumber)

        elif inp ==0:
            self.getInformation(print_)

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
        add=Inp4()
        airplane=createAirplane()
        airplane=add.addAirplaneInp(airplane)
        if airplane == 0:
            self.create(print_)
        else:
            UI.UIsaveAircraft(airplane)


    def copyExistingVoyage(self,print_):
        print_.window6()


    def createNewVoyage(self,print_):
        print_.window7()
        add=Inp3()
        departureFlight=createFlightRoute()
        [departureFlight,soldTick]=add.addRouteInp(departureFlight)
        if departureFlight == 0:
            self.createVoyages(print_)
        else:
            returnFlight = createFlightRoute()
            departureFlight.departingFrom="KEF"
            returnFlight.flightNumber=departureFlight.flightNumber
            returnFlight.departingFrom = departureFlight.arrivingAt
            returnFlight.arrivingAt = departureFlight.departingFrom
            returnFlight.departure = add_hour(departureFlight.arrival,1)
            returnFlight.aircraftId=departureFlight.aircraftId
            returnFlight.soldTickets=soldTick
            depFlArr=int(getHour(departureFlight.arrival))
            # depFlDep=int(getHour(departureFlight.departure))
            # flyingTime=depFlArr-depFlDep
            returnFlight.arrival = add_hour(returnFlight.departure,2)
            voyage=createVoyage(departureFlight,returnFlight)
            UI.UIsaveVoyage(voyage)



    def copyExistingVoyage(self,print_):
        print_.window16()
        input_string=input("Flight number: ")
        if str(input_string) == 'CANCEL':
            self.createVoyages(print_)
        else:
            voyage=UI.UIgettingVoyage(input_string)
            print_.window27()
            inp=int(input("Type Number: "))
            print_.window28()
            inpYear=int(input("Year: "))
            inpMonth=int(input("Month: "))
            inpDay=int(input("Day: "))
            inpHour=int(input("Hour: "))
            inpMinute=int(input("Minute: "))
            date=getDate(inpYear,inpMonth,inpDay,inpHour,inpMinute)
            voyage.departureFlight.departure=date
            voyage.departureFlight.arrival=add_hour(date,3)
            voyage.returnFlight.departure=add_hour(date,4)
            voyage.returnFlight.arrival=add_hour(date,6)
            UI.UIcopyExistingVoyage(voyage,inp,date)



    def createVoyages(self,print_):
        print_.window5()
        inp=int(input("number: "))
        if inp==1:
            self.copyExistingVoyage(print_)
        elif inp==2:
            self.createNewVoyage(print_)
        elif inp==0:
            self.create(print_)

    def createNewStaff(self,print_):
        print_.window3()
        employee = createStaff()
        add=Inp1()
        empl=add.addStaffInp1(employee)
        if empl == 0:
            self.create(print_)
        else:
            UI.UIsaveStaff(empl)

    # def createNewCabin(self,print_):
    #     print_.window4()
    #     add=Inp()
    #     [name,ssn,address,phoneNumber,mobileNumber,emailAddress,rank]=add.addStaffInp()
    #     cabin=createStaff(name,ssn,address,phoneNumber,mobileNumber,emailAddress,rank,"N/A")
    #     UI.UIsaveCabin(cabin)


    def createNewStaffmember(self,print_):
        self.createNewStaff(print_)

    def createDestinations(self, print_):
        print_.window8()
        add = Inp2()
        dest = CreateDestination()
        newDest=add.addDestinationInp(dest)
        if newDest == 0:
            self.create(print_)
        else:
            UI.UIsaveDestinationInFile(newDest)

    def create(self,print_):
        print_.window1() #Staff,voyage,destination,airplane
        inp=int(input("number: "))
        if inp==1:  #Staff valinn
            self.createNewStaffmember(print_)
        elif inp==2:
            self.createVoyages(print_)
        elif inp==3:
            self.createDestinations(print_)
        elif inp==4:
            self.createAirplanes(print_)
        elif inp==0:
            self.mainMenu()


    def mainMenu(self):
        path = 'PastFlights copy.csv'
        file = OpenFile(path)
        originalFlights = read_pastFlights(file)
        destinations = getDestinations()
        newFlights = fixFlNo(originalFlights, destinations)
        updateFlights(newFlights, path)
        path = 'UpcomingFlights copy3.csv'
        file = OpenFile(path)
        originalFlights = read_pastFlights(file)
        destinations = getDestinations()
        newFlights = fixFlNo(originalFlights, destinations)
        updateFlights(newFlights, path)

        print_=pagePrints(100,40)
        print_.frontPage() #'c', 'g', 'u'
        inp=input()
        if inp=="c":
            self.create(print_)
        elif inp=='g':  #Get information
            self.getInformation(print_) #Staff,airplanes,voyage,destinations
        elif inp=='u':
            self.updateInformation(print_)
