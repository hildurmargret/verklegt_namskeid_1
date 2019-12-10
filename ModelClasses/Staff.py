from DataLayer.saveStaffInFile import*
class createStaff:

    def __init__(self,name,ssn,address,phoneNumber,emailAddress,rank,role,licence):
      self.name=name
      self.SSN=ssn
      self.address=address
      self.phoneNumber=phoneNumber
      self.emailAddress=emailAddress
      self.licence=licence
      self.rank=rank
      self.role=role
      self.cancel=0


# class createPilot(createStaff):
#     def __init__(self,name,ssn,address,phoneNumber,emailAddress,rank,role,licence):
#         super().__init__(name,ssn,address,phoneNumber,emailAddress,rank,role,licence)
#         self.licence=licence
#         #savePilotInFile(self.SSN,self.name,self.rank,self.licence,self.phoneNumber)
#
# class createCabin(createStaff):
#     def __init__(self,name,ssn,address,phoneNumber,emailAddress,rank,role):
#         super().__init__(name,ssn,address,phoneNumber,emailAddress,rank,role)
        #saveCabinInFile(self.SSN,self.name,self.rank,self.licence,self.phoneNumber)
