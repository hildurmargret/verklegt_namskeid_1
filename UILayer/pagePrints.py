

class pagePrints:
    def __init__(self,cols,rows):
        self.cols=cols
        self.rows=rows

    def prentButton(self,bil,merki,ord):
        print("#",end=" ")
        for _ in range(bil):
            print(" ",end="")
        for _ in range(merki):
            print("#",end=" ")
        for _ in range(bil):
            print(" ",end="")
        print("#")

        print("#",end=" ")
        for _ in range(bil):
            print(" ",end="")
        print("#",end=" ")
        for _ in range(2*merki-4):
            print(" ",end="")
        print("#",end=" ")
        for _ in range(bil):
            print(" ",end="")
        print("#",end=" ")

        print("#",end=" ")
        for _ in range(bil):
            print(" ",end="")
        print("#",end=" ")
        print(ord,end=" ")
        print("#",end=" ")
        for _ in range(bil):
            print(" ",end="")
        print("#")

        print("#",end=" ")
        for _ in range(bil):
            print(" ",end="")
        print("#",end=" ")
        for _ in range(2*merki-4):
            print(" ",end="")
        print("#",end=" ")
        for _ in range(bil):
            print(" ",end="")
        print("#")

        print("#",end=" ")
        for _ in range(bil):
            print(" ",end="")
        for _ in range(merki):
            print("#",end=" ")
        for _ in range(bil):
            print(" ",end="")
        print("#")

    def prentSpace(self,linur,breidd):
        breidd=int(breidd)
        for _ in range(linur):
            print("#",end=" ")
            for _ in range(breidd-2):
                print(" ",end=" ")
            print("#",end=" ")


    def prentLina(self,breidd):
        breidd=int(breidd)
        for _ in range(breidd):
            print("#",end=" ")
        print()

    def prentWord(self,bil,ord):
        print("#",end=" ")
        for _ in range(bil):
            print(" ",end=" ")
        print(ord,end=" ")
        for _ in range(95-2*bil-len(ord)):
            print(" ",end="")
        print("#")

    def frontPage(self):
        self.prentLina((self.cols)/2)
        self.prentSpace(10,(self.cols)/2)
        self.prentButton(36,12,"    Create new     ")
        self.prentButton(36,12,"  Get information  ")
        self.prentButton(36,12,"       Update      ")
        self.prentSpace(10,(self.cols)/2)
        self.prentWord(7,"Please choose ['c' create, 'g' get, 'u' update]")
        self.prentSpace(1,(self.cols)/2)
        self.prentLina((self.cols)/2)

    def window1(self):
        self.prentLina((self.cols)/2)
        self.prentSpace(14,(self.cols)/2)
        self.prentWord(15,"1: New staffmember")
        self.prentWord(15,"2: New voyage")
        self.prentWord(15,"3: New destination")
        self.prentWord(15,"4: New airplane")
        self.prentSpace(1,(self.cols)/2)
        self.prentWord(15,"0: Back")
        self.prentSpace(13,(self.cols)/2)
        self.prentWord(15,"Please choose [1,2,3 or 4] ")
        self.prentSpace(3,(self.cols)/2)
        self.prentLina((self.cols)/2)

    def window2(self):
        self.prentLina((self.cols)/2)
        self.prentSpace(15,(self.cols)/2)
        self.prentWord(15,"1: Pilot")
        self.prentWord(15,"2: Cabin crew")
        self.prentSpace(1,(self.cols)/2)
        self.prentWord(15,"0: Back")
        self.prentSpace(14,(self.cols)/2)
        self.prentWord(15,"Please choose [1 or 2] ")
        self.prentSpace(3,(self.cols)/2)
        self.prentLina((self.cols)/2)

    def window3(self):
        self.prentLina((self.cols)/2)
        self.prentSpace(11,(self.cols)/2)
        self.prentWord(15,"Adding new pilot")
        self.prentSpace(1,(self.cols)/2)
        self.prentWord(15,"Name")
        self.prentWord(15,"SSN")
        self.prentWord(15,"Address")
        self.prentWord(15,"Phone number")
        self.prentWord(15,"Mobile number")
        self.prentWord(15,"Email address")
        self.prentWord(15,"Role")
        self.prentWord(15,"Rank")
        self.prentWord(15,"Airplane licence")
        self.prentSpace(1,(self.cols)/2)
        self.prentWord(15,"Type 'CANCEL' to cancel")
        self.prentSpace(10,(self.cols)/2)
        self.prentWord(15,"Type in the information")
        self.prentSpace(2,(self.cols)/2)
        self.prentLina((self.cols)/2)

    def window4(self):
        self.prentLina((self.cols)/2)
        self.prentSpace(11,(self.cols)/2)
        self.prentWord(15,"Adding new Cabin crew")
        self.prentSpace(1,(self.cols)/2)
        self.prentWord(15,"Name")
        self.prentWord(15,"SSN")
        self.prentWord(15,"Address")
        self.prentWord(15,"Phone number")
        self.prentWord(15,"Mobile number")
        self.prentWord(15,"Email address")
        self.prentWord(15,"Role")
        self.prentWord(15,"Rank")
        self.prentSpace(1,(self.cols)/2)
        self.prentWord(15,"Type 'CANCEL' to cancel")
        self.prentSpace(11,(self.cols)/2)
        self.prentWord(15,"Type in the information")
        self.prentSpace(2,(self.cols)/2)
        self.prentLina((self.cols)/2)

    def window5(self):
        self.prentLina((self.cols)/2)
        self.prentSpace(15,(self.cols)/2)
        self.prentWord(15,"1: Copy existing voyage")
        self.prentWord(15,"2: Create new voyage")
        self.prentSpace(1,(self.cols)/2)
        self.prentWord(15,"0: Back")
        self.prentSpace(14,(self.cols)/2)
        self.prentWord(15,"Please choose [1 or 2] ")
        self.prentSpace(3,(self.cols)/2)
        self.prentLina((self.cols)/2)

    def window6(self):
        self.prentLina((self.cols)/2)
        self.prentSpace(18,(self.cols)/2)
        self.prentWord(15,"Choose a number")
        self.prentSpace(18,(self.cols)/2)
        self.prentLina((self.cols)/2)


    def window7(self):
        self.prentLina((self.cols)/2)
        self.prentSpace(12,(self.cols)/2)
        self.prentWord(15,"Flight number")
        self.prentWord(15,"Departing from")
        self.prentWord(15,"Arriving at")
        self.prentWord(15,"Departure timing")
        self.prentWord(15,"Number of cabin")
        self.prentWord(15,"Number of pilots")
        self.prentWord(15,"Aircraft Id")
        self.prentSpace(1,(self.cols)/2)
        self.prentWord(15,"Type 'CANCEL' to cancel")
        self.prentSpace(12,(self.cols)/2)
        self.prentWord(15,"Type in the information")
        self.prentSpace(3,(self.cols)/2)
        self.prentLina((self.cols)/2)


    def window8(self):
        self.prentLina((self.cols)/2)
        self.prentSpace(14,(self.cols)/2)
        self.prentWord(15,"Destination Id")
        self.prentWord(15,"Destination town")
        self.prentWord(15,"Country")
        self.prentWord(15,"Distance from Iceland")
        self.prentWord(15,"Airport")
        self.prentWord(15,"Contact name")
        self.prentWord(15,"Contact phone number")
        self.prentSpace(1,(self.cols)/2)
        self.prentWord(15,"Type 'CANCEL' to cancel")
        self.prentSpace(11,(self.cols)/2)
        self.prentWord(15,"Type in the information")
        self.prentSpace(3,(self.cols)/2)
        self.prentLina((self.cols)/2)

    def window9(self):
        self.prentLina(self.cols/2)
        self.prentSpace(9,(self.cols)/2)
        self.prentWord(15,"Plane type ID")
        self.prentWord(15,"Airplane manufacturer")
        self.prentWord(15,"Airplane model")
        self.prentWord(15,"Capacity")
        self.prentWord(15,"Empty weight")
        self.prentWord(15,"Max take off weight")
        self.prentWord(15,"Unit thrus")
        self.prentWord(15,"Service ceiling")
        self.prentWord(15,"Length")
        self.prentWord(15,"Height")
        self.prentWord(15,"Wingspan")
        self.prentSpace(1,(self.cols)/2)
        self.prentWord(15,"Type 'CANCEL' to cancel")
        self.prentSpace(11,(self.cols)/2)
        self.prentWord(15,"Type in the information")
        self.prentSpace(3,(self.cols)/2)
        self.prentLina((self.cols)/2)


    def window10(self):
        self.prentLina(self.cols/2)
        self.prentSpace(15,(self.cols)/2)
        self.prentWord(15,"1: Staff")
        self.prentWord(15,"2: Airplanes")
        self.prentWord(15,"3: Voyages")
        self.prentWord(15,"4: Destinations")
        self.prentSpace(1,(self.cols)/2)
        self.prentWord(15,"0: Back")
        self.prentSpace(12,(self.cols)/2)
        self.prentWord(15,"Please choose [1,2,3 or 4]")
        self.prentSpace(3,(self.cols)/2)
        self.prentLina((self.cols)/2)

    def window11(self):
        self.prentLina(self.cols/2)
        self.prentSpace(13,(self.cols)/2)
        self.prentWord(15,"1: All employees")
        self.prentWord(15,"2: All pilots")
        self.prentWord(15,"3: All Cabin crew")
        self.prentWord(15,"4: Search for an employee")
        self.prentWord(15,"5: Employee destinations")
        self.prentWord(15,"6: Employee work schedule ")
        self.prentWord(15,"7: Employees available now")
        self.prentWord(15,"8: Employees working by date")
        self.prentSpace(1,(self.cols)/2)
        self.prentWord(15,"0: Back")
        self.prentSpace(10,(self.cols)/2)
        self.prentWord(15,"Please choose [1,2,3,4,5,6,7 or 8]")
        self.prentSpace(3,(self.cols)/2)
        self.prentLina((self.cols)/2)

    def window12(self):
        self.prentLina((self.cols)/2)
        self.prentSpace(17,(self.cols)/2)
        self.prentWord(15,"Search for employee by name or SSN")
        self.prentSpace(1,(self.cols)/2)
        self.prentWord(15,"Type 'CANCEL' to cancel")
        self.prentSpace(17,(self.cols)/2)
        self.prentLina((self.cols)/2)

    def window13(self):
        self.prentLina((self.cols)/2)
        self.prentSpace(18,(self.cols)/2)
        self.prentWord(15,"Save work schedule?")
        self.prentSpace(1,(self.cols)/2)
        self.prentSpace(12,(self.cols)/2)
        self.prentWord(15,"1: Save")
        self.prentWord(15,"0: Don't save")
        self.prentSpace(3,(self.cols)/2)
        self.prentLina((self.cols)/2)

    def window14(self):
        self.prentLina((self.cols)/2)
        self.prentSpace(14,(self.cols)/2)
        self.prentWord(15,"1: All airplanes")
        self.prentWord(15,"2: All pilots by airplane licence")
        self.prentWord(15,"3: Search for pilots by licence")
        self.prentWord(15,"4: See states of all airplanes")
        self.prentSpace(1,(self.cols)/2)
        self.prentWord(15,"0: Back")
        self.prentSpace(13,(self.cols)/2)
        self.prentWord(15,"Please choose [1,2,3 or 4] ")
        self.prentSpace(3,(self.cols)/2)
        self.prentLina((self.cols)/2)

    def window15(self):
        self.prentLina((self.cols)/2)
        self.prentSpace(14,(self.cols)/2)
        self.prentWord(15,"1: Search for a voyage")
        self.prentWord(15,"2: Search for voyages by date")
        self.prentWord(15,"3: Search for voyages by week")
        self.prentWord(15,"4: See voyage states")
        self.prentSpace(1,(self.cols)/2)
        self.prentWord(15,"0: Back")
        self.prentSpace(13,(self.cols)/2)
        self.prentWord(15,"Please choose [1,2,3 or 4] ")
        self.prentSpace(3,(self.cols)/2)
        self.prentLina((self.cols)/2)

    def window16(self):
        self.prentLina((self.cols)/2)
        self.prentSpace(18,(self.cols)/2)
        self.prentWord(15,"Type in a flight number")
        self.prentSpace(1,(self.cols)/2)
        self.prentSpace(17,(self.cols)/2)
        self.prentLina((self.cols)/2)

    def window17(self):
        self.prentLina((self.cols)/2)
        self.prentSpace(18,(self.cols)/2)
        self.prentWord(15,"Type in date (dd/mm/yyyy)")
        self.prentSpace(1,(self.cols)/2)
        self.prentSpace(17,(self.cols)/2)
        self.prentLina((self.cols)/2)

    #TAKA UT?
    def window18(self):
        self.prentLina((self.cols)/2)
        self.prentSpace(18,(self.cols)/2)
        self.prentWord(15,"Type in name of the voyage")
        self.prentSpace(1,(self.cols)/2)
        self.prentSpace(17,(self.cols)/2)
        self.prentLina((self.cols)/2)

    def window19(self):
        self.prentLina((self.cols)/2)
        self.prentSpace(18,(self.cols)/2)
        self.prentWord(15,"Type a week (1-52) and a year")
        self.prentSpace(1,(self.cols)/2)
        self.prentSpace(17,(self.cols)/2)
        self.prentLina((self.cols)/2)

    def window20(self):
        self.prentLina((self.cols)/2)
        self.prentSpace(15,(self.cols)/2)
        self.prentWord(15,"1: All destinations in alphabetical order")
        self.prentWord(15,"2: Most popular destination")
        self.prentSpace(1,(self.cols)/2)
        self.prentWord(15,"0: Back")
        self.prentSpace(14,(self.cols)/2)
        self.prentWord(15,"Please choose [1 or 2] ")
        self.prentSpace(3,(self.cols)/2)
        self.prentLina((self.cols)/2)

    def window21(self):
        self.prentLina((self.cols)/2)
        self.prentSpace(14,(self.cols)/2)
        self.prentWord(15,"1: Employees")
        self.prentWord(15,"2: Destination informations")
        self.prentWord(15,"3: Appoint employees to voyages")
        self.prentWord(15,"4: Voyage")
        self.prentSpace(1,(self.cols)/2)
        self.prentWord(15,"0: Back")
        self.prentSpace(13,(self.cols)/2)
        self.prentWord(15,"Please choose [1,2,3 or 4] ")
        self.prentSpace(3,(self.cols)/2)
        self.prentLina((self.cols)/2)

    def window22(self):
        self.prentLina((self.cols)/2)
        self.prentSpace(15,(self.cols)/2)
        self.prentWord(15,"Type in destination to update")
        self.prentSpace(1,(self.cols)/2)
        self.prentWord(15,"0: Back")
        self.prentSpace(16,(self.cols)/2)
        self.prentSpace(3,(self.cols)/2)
        self.prentLina((self.cols)/2)

    def window23(self):
        self.prentLina((self.cols)/2)
        self.prentSpace(12,(self.cols)/2)
        self.prentWord(15,"Update pilot:")
        self.prentSpace(1,(self.cols)/2)
        self.prentWord(15,"Name")
        self.prentWord(15,"SSN")
        self.prentWord(15,"Address")
        self.prentWord(15,"Phone number")
        self.prentWord(15,"Mobile number")
        self.prentWord(15,"Email address")
        self.prentWord(15,"Role")
        self.prentWord(15,"Rank")
        self.prentWord(15,"Airplane licence")
        self.prentSpace(1,(self.cols)/2)
        self.prentWord(15,"Type 'CANCEL' to cancel")
        self.prentSpace(10,(self.cols)/2)
        self.prentSpace(2,(self.cols)/2)
        self.prentLina((self.cols)/2)

    def window24(self):
        self.prentLina((self.cols)/2)
        self.prentSpace(11,(self.cols)/2)
        self.prentWord(15,"Update Cabin crew:")
        self.prentSpace(1,(self.cols)/2)
        self.prentWord(15,"Name")
        self.prentWord(15,"SSN")
        self.prentWord(15,"Address")
        self.prentWord(15,"Phone number")
        self.prentWord(15,"Mobile number")
        self.prentWord(15,"Email address")
        self.prentWord(15,"Role")
        self.prentWord(15,"Rank")
        self.prentSpace(1,(self.cols)/2)
        self.prentWord(15,"Type 'CANCEL' to cancel")
        self.prentSpace(11,(self.cols)/2)
        self.prentWord(15,"Type in the information")
        self.prentSpace(2,(self.cols)/2)
        self.prentLina((self.cols)/2)

    def window25(self):
        self.prentLina((self.cols)/2)
        self.prentSpace(18,(self.cols)/2)
        self.prentWord(15,"Type in an airplane type")
        self.prentSpace(1,(self.cols)/2)
        self.prentSpace(17,(self.cols)/2)
        self.prentLina((self.cols)/2)

    def window26(self):
        self.prentLina((self.cols)/2)
        self.prentSpace(18,(self.cols)/2)
        self.prentWord(15,"1: Weekly work schedule")
        self.prentWord(15,"2: Complete work schedule")
        self.prentSpace(1,(self.cols)/2)
        self.prentWord(15,"0: Back")
        self.prentSpace(15,(self.cols)/2)
        self.prentLina((self.cols)/2)

    def window27(self):
        self.prentLina((self.cols)/2)
        self.prentSpace(17,(self.cols)/2)
        self.prentWord(15,"1: Once")
        self.prentWord(15,"2: Daily")
        self.prentWord(15,"3: Weekly")
        self.prentSpace(17,(self.cols)/2)
        self.prentLina((self.cols)/2)

    def window28(self):
        self.prentLina((self.cols)/2)
        self.prentSpace(19,(self.cols)/2)
        self.prentWord(15,"Type in information about departure date")
        self.prentSpace(17,(self.cols)/2)
        self.prentLina((self.cols)/2)
