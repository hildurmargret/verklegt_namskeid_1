class Staff:

    def __init__(self):
      self.name=""
      self.SSN=0
      self.address=""
      self.phoneNumber=0
      self.mobileNumber=0
      self.emailAddress=""
      self.airplaneLicense=""
      self.rank=""

    def addInfo(self):
        self.name=input("Name: ")
        self.SSN=input("SSN: ")
        self.address=input("Address: ")
        self.phoneNumber=input("Phone number: ")
        self.mobileNumber=input("Mobile number: ")
        self.enailAddress=input("Email address: ")
        self.rank=input("Rank: ")

class Pilot(Staff):
    def __init__(self):
        super().__init__()
        self.rank=""
    def addInfo(self):
        super().addInfo()
        self.airplaneLicense=input("Airplane license: ")

#class FlightAttendant(Staff):
    pass
