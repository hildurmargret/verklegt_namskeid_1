from LogicLayer.LL_API import*
from UILayer.printAirplanes import*

LL=LL_API()

class UI_Manager:

    def __init__(self):
        pass

    def UIsaveCabin(self,newStaff):
        LL.LLsaveCabin(newStaff)

    def UIsavePilot(self,newStaff):
        LL.LLsavePilot(newStaff)

    def UIsaveVoyage(self,newVoyage):
        LL.LLsaveVoyage(newVoyage)

    def UIsaveAircraft(self):
        LL.LLsaveAircraft(newAircraft)

    def UIsaveDestinationInFile(self):
        LL.LLsaveDestination(NewDest)

    def UIgettingAirplanes(self):
        getAircraft = LL.LLgetAircraft()
        printAircraft(getAircraft)
