class updateStaffInput():

    def addStaffInp(self,employee):
        name=input("Name: ")
        if name=="":
            self.name=employee.name
        else:
            self.name=name
        SSN=input("SSN: ")
        if SSN=="":
            self.SSN=employee.SSN
        else:
            self.SSN=SSN
        address=input("Address: ")
        if address=="":
            self.address=employee.address
        else:
            self.address=address
        phoneNumber=input("Phone number: ")
        if phoneNumber=="":
            self.phoneNumber=employee.phoneNumber
        else:
            self.phoneNumber=phoneNumber
        emailAddress=input("Email address: ")
        if emailAddress=="":
            self.emailAddress=employee.emailAddress
        else:
            self.emailAddress=emailAddress
        role=input("Role: ")
        if role=="":
            self.role=employee.role
        else:
            self.role=role
        rank=input("Rank: ")
        if rank=="":
            self.rank=employee.rank
        else:
            self.rank=rank
        if rank=="Pilot":
            licence=input("licence: ")
            if licence=="":
                self.licence=employee.licence
            else:
                self.licence=licence
        else:
            self.licence=employee.licence
        return self
