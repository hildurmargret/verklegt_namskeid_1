from LogicLayer.LL_API import*
from UILayer.printAirplanes import*
from UILayer.updateStaff_Input import*
from UILayer.chooseEmplFromList import*
from UILayer.updateDestination_input import*
from UILayer.addInp1 import*
from UILayer.addInp3 import*
from UILayer.chooseDestinationFromList import*
from LogicLayer.leitaVoyage import*

LL=LL_API()

class UI_Manager:

    def __init__(self):
        pass

    def UIsaveStaff(self,newStaff):
        LL.LLsaveStaff(newStaff)

    #def UIsavePilot(self,newPilot):
    #    LL.LLsavePilot(newPilot)

    def UIsaveVoyage(self,newVoyage):
        LL.LLsaveVoyage(newVoyage)

    def UIsaveAircraft(self,newAircraft):
        LL.LLsaveAircraft(newAircraft)

    def UIsaveDestinationInFile(self, NewDest):
        LL.LLsaveDestination(NewDest)

    def UIgettingAirplanes(self):
        getAircraft = LL.LLgetAircraft()
        printAircraft(getAircraft)

    def UIgettingVoyage(self,input_string):
        voyage=LL.LLgettingVoyage(input_string)
        return voyage

    def UIupdateStaff(self):
        update=Inp1()
        input_string=input("SSN: ")
        employees=LL.LLupdateStaff(input_string)
        employee=pilotsFromList(employees)
        employee=update.addStaffInp1(employee)
        LL.LLupdatingStaff(employee)


    # def UIupdateCabin(self):
    #     update=updateStaffInput()
    #     input_string=input("SSN: ")
    #     employees=LL.LLupdateStaff(input_string)
    #     employee=cabinFromList(employees)
    #     employee=update.addStaffInp(employee)
    #     LL.LLupdatingStaff(employee)

    def UIupdateDestination(self):
        update=updateDestInput()
        dest=LL.LLupdateDestination()
        dest=DestinationFromList(dest)
        dest=update.addDestInp(dest)
        print(dest)
        LL.LLupdatingDestination(dest)

    def UIupdateAircraft(self):
        update=Inp4()
        aircrafts=self.UIgettingAirplanes()
        aircraft=aircraftFromList(aircrafts)
        aircraft=update.addAirplaneInp(aircraft)
        LL.LLupdateAircraft(aircraft)

    def UIupdateVoyage(self):
        update=Inp3()
        input_string = input('Departing flight number: ')
        voyage=leitaVoyage(input_string)
        LL.LLupdateVoyage(voyage)

    def UIemployeesToVoyage(self):
        update=Inp3()
        input_string = input('Departing flight number: ')
        voyage=leitaVoyage(input_string)
        input_string=input("SSN: ")
        employees=LL.LLgettingEmployees(input_string)
        employee=emplFromList(employees)
        LL.LLemployeesToVoyage(voyage,employee)
