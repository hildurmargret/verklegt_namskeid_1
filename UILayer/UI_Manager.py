from LogicLayer.LL_API import*
from UILayer.printAirplanes import*
from UILayer.updateStaff_Input import*
from UILayer.chooseEmplFromList import*

LL=LL_API()

class UI_Manager:

    def __init__(self):
        pass

    def UIsaveCabin(self,newCabin):
        LL.LLsaveCabin(newCabin)

    def UIsavePilot(self,newPilot):
        LL.LLsavePilot(newPilot)

    def UIsaveVoyage(self,newVoyage):
        LL.LLsaveVoyage(newVoyage)

    def UIsaveAircraft(self,newAircraft):
        LL.LLsaveAircraft(newAircraft)

    def UIsaveDestinationInFile(self, NewDest):
        LL.LLsaveDestination(NewDest)

    def UIgettingAirplanes(self):
        getAircraft = LL.LLgetAircraft()
        printAircraft(getAircraft)

    def UIupdatePilot(self):
        update=updateStaffInput()
        input_string=input("SSN: ")
        employees=LL.LLupdateStaff(input_string)
        employee=pilotsFromList(employees)
        employee=update.addStaffInp(employee)
        LL.LLupdatingStaff(employee)


    def UIupdateCabin(self):
        update=updateStaffInput()
        input_string=input("SSN: ")
        employees=LL.LLupdateStaff(input_string)
        employee=cabinFromList(employees)
        employee=update.addStaffInp(employee)
        LL.LLupdatingStaff(employee)
