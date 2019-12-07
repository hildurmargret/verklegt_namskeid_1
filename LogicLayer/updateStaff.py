class updateStaff():
    def addStaff(self):
        self.name=input("Name: ")
        if self.name=="CANCEL":
            self.cancel=1
            return 0
        self.SSN=input("SSN: ")
        if self.SSN=="CANCEL":
            self.cancel=1
            return 0
        self.address=input("Address: ")
        if self.address=="CANCEL":
            self.cancel=1
            return 0
        self.phoneNumber=input("Phone number: ")
        if self.phoneNumber=="CANCEL":
            self.cancel=1
            return 0
        self.mobileNumber=input("Mobile number: ")
        if self.mobileNumber=="CANCEL":
            self.cancel=1
            return 0
        self.emailAddress=input("Email address: ")
        if self.emailAddress=="CANCEL":
            self.cancel=1
            return 0
        self.rank=input("Rank: ")
        if self.rank=="CANCEL":
            self.cancel=1
            return 0

class Pilot(Staff):
    def addInfo(self):
        super().addInfo()
        if self.cancel!=1:
            self.airplaneLicense=input("Airplane licence: ")
        savePilotInFile(self.SSN,self.name,self.rank,self.airplaneLicence,self.phoneNumber)

class Cabin(Staff):
    def addInfo(self):
        super().addInfo()
        saveCabinInFile(self.SSN,self.name,self.rank,self.airplaneLicence,self.phoneNumber)
