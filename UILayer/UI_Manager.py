from LogicLayer.LL_API import*
from UILayer.printAirplanes import*

LL=LL_API()

class UI_Manager:

    def __init__(self):
        pass

    def UIsaveCabin(self):
        LLsaveCabin(newStaff)

    def UIsavePilot(self):
        LLsavePilot(newStaff)

    def UIsaveVoyage(self):
        LLsaveVoyage(newVoyage)

    def UIsaveAircraft(self):
        LLsaveAircraft(newAircraft)

    def UIsaveDestinationInFile(self):
        LLsaveDestination(NewDest)

    def UIgettingAirplanes(self):
        getAircraft = LL.LLgetAircraft()
        printAircraft(getAircraft)
