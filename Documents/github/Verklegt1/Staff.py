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
        self.name=raw_input("Name: ")
        self.SSN=raw_input("SSN: ")
        self.address=raw_input("Address: ")
        self.phoneNumber=raw_input("Phone number: ")
        self.mobileNumber=raw_input("Mobile number: ")
        self.enailAddress=raw_input("Email address: ")
        self.airplaneLicense=raw_input("Airplane license: ")
        self.rank=raw_input("Rank: ")
