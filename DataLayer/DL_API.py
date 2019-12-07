class DL_API():

    def flightAttendant(self,print_):
        new_staff=Cabin()
        print_.window4() #Pilot,flight attendant; info
        new_staff.addInfo()

    def pilot(self):
        new_pilot=Pilot()
        print_.window3() #Adding new pilot; info
        new_pilot.addInfo()
