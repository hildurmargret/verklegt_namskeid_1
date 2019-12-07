from DataLayer.saveStaffInFile import*
class createStaff:

    def __init__(self,name,ssn,address,phoneNumber,mobileNumber,emailAddress,rank,airplaneLicense):
      self.name=name
      self.SSN=ssn
      self.address=address
      self.phoneNumber=phoneNumber
      self.mobileNumber=mobileNumber
      self.emailAddress=emailAddress
      self.airplaneLicence=airplaneLicense
      self.rank=rank
      self.cancel=0


class createPilot(createStaff):
    def __init__(self,name,ssn,address,phoneNumber,mobileNumber,emailAddress,rank,airplaneLicense):
        super().__init__(name,ssn,address,phoneNumber,mobileNumber,emailAddress,rank,airplaneLicense)
        self.airplaneLicence=airplaneLicence
        savePilotInFile(self.SSN,self.name,self.rank,self.airplaneLicence,self.phoneNumber)

class createCabin(createStaff):
    def __init__(self,name,ssn,address,phoneNumber,mobileNumber,emailAddress,rank):
        super().__init__(name,ssn,address,phoneNumber,mobileNumber,emailAddress,rank)
        saveCabinInFile(self.SSN,self.name,self.rank,self.airplaneLicence,self.phoneNumber)
