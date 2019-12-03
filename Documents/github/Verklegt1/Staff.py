class Staff:

    def __init__(self):
      self.name=""
      self.SSN=0
      self.address=""
      self.phoneNumber=0
      self.mobileNumber=0
      self.emailAddress=""
      self.rank=""
      self.airplaneLicence=""
      self.cancel=0

    def addInfo(self):
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
