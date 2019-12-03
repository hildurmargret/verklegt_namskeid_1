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

    def addInfo(self):
        self.name=input("Name: ")
        self.SSN=input("SSN: ")
        self.address=input("Address: ")
        self.phoneNumber=input("Phone number: ")
        self.mobileNumber=input("Mobile number: ")
        self.enailAddress=input("Email address: ")
        self.rank=input("Rank: ")

class Pilot(Staff):
    def addInfo(self):
        super().addInfo()
        self.airplaneLicence=input("Airplane licence: ")
