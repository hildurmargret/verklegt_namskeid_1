#from Date import*
#from getPilotsByAirplanes import*
#from getPilotsByLicence import*

#def PilotsByAirplanes()

from UILayer.Windows import*
from DataLayer.saveStaffInFile import*
from DataLayer.saveAircraftInFile import*
class LL_API():
    def LLsaveCabin(newStaff):
        DLsaveCabin(newStaff)
    def LLsavePilot(newStaff):
        DLsavePilot(newStaff)
    def saveAircraft(newAircraft):
        saveAircraftInFile(newAircraft)
