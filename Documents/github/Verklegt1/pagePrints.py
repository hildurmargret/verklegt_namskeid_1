import sys

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
        self.prentWord(15,"b: Back")
        self.prentSpace(13,(self.cols)/2)
        self.prentWord(15,"Please choose [1,2,3 or 4] ")
        self.prentSpace(3,(self.cols)/2)
        self.prentLina((self.cols)/2)

    def window2(self):
        self.prentLina((self.cols)/2)
        self.prentSpace(15,(self.cols)/2)
        self.prentWord(15,"1: Pilot")
        self.prentWord(15,"2: Flight attendant")
        self.prentSpace(1,(self.cols)/2)
        self.prentWord(15,"b: Back")
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
        self.prentWord(15,"Rank")
        self.prentWord(15,"Airplane license")
        self.prentSpace(1,(self.cols)/2)
        self.prentWord(15,"Type 'CANCEL' to cancel")
        self.prentSpace(10,(self.cols)/2)
        self.prentWord(15,"Type in the information")
        self.prentSpace(3,(self.cols)/2)
        self.prentLina((self.cols)/2)

    def window4(self):
        self.prentLina((self.cols)/2)
        self.prentSpace(11,(self.cols)/2)
        self.prentWord(15,"Adding new flight attendant")
        self.prentSpace(1,(self.cols)/2)
        self.prentWord(15,"Name")
        self.prentWord(15,"SSN")
        self.prentWord(15,"Address")
        self.prentWord(15,"Phone number")
        self.prentWord(15,"Mobile number")
        self.prentWord(15,"Email address")
        self.prentWord(15,"Rank")
        self.prentSpace(1,(self.cols)/2)
        self.prentWord(15,"Type 'CANCEL' to cancel")
        self.prentSpace(11,(self.cols)/2)
        self.prentWord(15,"Type in the information")
        self.prentSpace(3,(self.cols)/2)
        self.prentLina((self.cols)/2)

    def window5(self):
        self.prentLina((self.cols)/2)
        self.prentSpace(15,(self.cols)/2)
        self.prentWord(15,"1: Copy existing voyage")
        self.prentWord(15,"2: Create new voyage")
        self.prentSpace(1,(self.cols)/2)
        self.prentWord(15,"b: Back")
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
        self.prentSpace(14,(self.cols)/2)
        self.prentWord(15,"Voyage title")
        self.prentWord(15,"Airplane name")
        self.prentWord(15,"Number of pilots needed")
        self.prentWord(15,"Number of cabin crew needed")
        self.prentWord(15,"Flight duration")
        self.prentSpace(1,(self.cols)/2)
        self.prentWord(15,"Type 'CANCEL' to cancel")
        self.prentSpace(12,(self.cols)/2)
        self.prentWord(15,"Type in the information")
        self.prentSpace(3,(self.cols)/2)
        self.prentLina((self.cols)/2)

    def window8(self):
        self.prentLina((self.cols)/2)
        self.prentSpace(14,(self.cols)/2)
        self.prentWord(15,"Country")
        self.prentWord(15,"Distance from Iceland")
        self.prentWord(15,"Airport")
        self.prentWord(15,"Contact name")
        self.prentWord(15,"Contact phone number")
        self.prentSpace(1,(self.cols)/2)
        self.prentWord(15,"Type 'CANCEL' to cancel")
        self.prentSpace(12,(self.cols)/2)
        self.prentWord(15,"Type in the information")
        self.prentSpace(3,(self.cols)/2)
        self.prentLina((self.cols)/2)

    def window9(self):
        self.prentLina(self.cols/2)
        self.prentSpace(15,(self.cols)/2)
        self.prentWord(15,"Airplane name")
        self.prentWord(15,"Airplane model")
        self.prentWord(15,"Airplane manufacturer")
        self.prentWord(15,"Number of passenger seats")
        self.prentSpace(1,(self.cols)/2)
        self.prentWord(15,"Type 'CANCEL' to cancel")
        self.prentSpace(12,(self.cols)/2)
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
        self.prentWord(15,"b: Back")
        self.prentSpace(12,(self.cols)/2)
        self.prentWord(15,"Please choose [1,2,3 or 4]")
        self.prentSpace(3,(self.cols)/2)
        self.prentLina((self.cols)/2)

    def window11(self):
        self.prentLina(self.cols/2)
        self.prentSpace(13,(self.cols)/2)
        self.prentWord(15,"1: List all employees")
        self.prentWord(15,"2: Information about all pilots")
        self.prentWord(15,"3: Information about all flight attendants")
        self.prentWord(15,"4: Search for specific employee")
        self.prentWord(15,"5: All destinations of a specific employee")
        self.prentWord(15,"6: Work schedule of a specific employee ")
        self.prentWord(15,"7: All employees that are not currently working")
        self.prentWord(15,"8: All employees that are working each day")
        self.prentSpace(1,(self.cols)/2)
        self.prentWord(15,"b: Back")
        self.prentSpace(10,(self.cols)/2)
        self.prentWord(15,"Please choose [1,2,3,4,5,6,7 or 8]")
        self.prentSpace(3,(self.cols)/2)
        self.prentLina((self.cols)/2)

    def window12(self):
        self.prentLina((self.cols)/2)
        self.prentSpace(18,(self.cols)/2)
        self.prentWord(15,"Type SSN of the employee")
        self.prentSpace(1,(self.cols)/2)
        self.prentSpace(17,(self.cols)/2)
        self.prentLina((self.cols)/2)

    def window13(self):
        self.prentLina((self.cols)/2)
        self.prentSpace(18,(self.cols)/2)
        self.prentWord(15,"Save work schedule")
        self.prentSpace(1,(self.cols)/2)
        self.prentSpace(17,(self.cols)/2)
        self.prentLina((self.cols)/2)

    def window14(self):
        self.prentLina((self.cols)/2)
        self.prentSpace(14,(self.cols)/2)
        self.prentWord(15,"1: Information on all airplanes")
        self.prentWord(15,"2: Employees certified for a specific airplane")
        self.prentWord(15,"3: List of pilots by airplane types")
        self.prentWord(15,"4: See states of all airplanes")
        self.prentSpace(1,(self.cols)/2)
        self.prentWord(15,"b: Back")
        self.prentSpace(13,(self.cols)/2)
        self.prentWord(15,"Please choose [1,2,3 or 4] ")
        self.prentSpace(3,(self.cols)/2)
        self.prentLina((self.cols)/2)

    def window15(self):
        self.prentLina((self.cols)/2)
        self.prentSpace(14,(self.cols)/2)
        self.prentWord(15,"1: Information about voyage")
        self.prentWord(15,"2: Information about voyage on a specific day")
        self.prentWord(15,"3: Information about voyage on a specific week")
        self.prentWord(15,"4: See states of the voyage")
        self.prentSpace(1,(self.cols)/2)
        self.prentWord(15,"b: Back")
        self.prentSpace(13,(self.cols)/2)
        self.prentWord(15,"Please choose [1,2,3 or 4] ")
        self.prentSpace(3,(self.cols)/2)
        self.prentLina((self.cols)/2)

    def window19(self):
        self.prentLina((self.cols)/2)
        self.prentSpace(15,(self.cols)/2)
        self.prentWord(15,"1: List all destinations in alphabetical order")
        self.prentWord(15,"2: List all destinations by popularity")
        self.prentSpace(1,(self.cols)/2)
        self.prentWord(15,"b: Back")
        self.prentSpace(14,(self.cols)/2)
        self.prentWord(15,"Please choose [1 or 2] ")
        self.prentSpace(3,(self.cols)/2)
        self.prentLina((self.cols)/2)
