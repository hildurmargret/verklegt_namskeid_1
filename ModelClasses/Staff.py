from DataLayer.saveStaffInFile import*
class createStaff:

    def __init__(self,name,ssn,address,phoneNumber,mobileNumber,emailAddress,rank,role,license):
      self.name=name
      self.SSN=ssn
      self.address=address
      self.phoneNumber=phoneNumber
      self.emailAddress=emailAddress
      self.licence=license
      self.rank=rank
      self.role=role
      self.cancel=0


class createPilot(createStaff):
    def __init__(self,name,ssn,address,phoneNumber,emailAddress,rank,role,license):
        super().__init__(name,ssn,address,phoneNumber,mobileNumber,emailAddress,rank,license)
        self.licence=licence
        savePilotInFile(self.SSN,self.name,self.rank,self.licence,self.phoneNumber)

class createCabin(createStaff):
    def __init__(self,name,ssn,address,phoneNumber,emailAddress,rank,role):
        super().__init__(name,ssn,address,phoneNumber,mobileNumber,emailAddress,rank)
        saveCabinInFile(self.SSN,self.name,self.rank,self.licence,self.phoneNumber)
