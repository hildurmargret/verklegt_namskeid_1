#!/usr/bin/env python3
from pagePrints import*
from Staff import*
from Voyage import*
from Destination import*

sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=40, cols=100))

print_=pagePrints(100,40)
print_.frontPage()

inp=input()

if inp=="c":

    print_.window1(); #Staff,voyage,destination,airplane
del inp
inp=int(input("number: "))

if inp==1:  #Staff valinn
    pilot=Pilot()
    staff=Staff()
    print_.window2();  #Pilot,flight attendant

    del inp
    inp=int(input("number: "))
    if inp==1:
        print_.window3(); #Adding new pilot; info
        pilot.addInfo()
    elif inp==2:

        print_.window4(); #Pilot,flight attendant; info
        staff.addInfo()

if inp==2:
    voyage=Voyage()
    print_.window5(); #Copy existing voyage,create new voyage
    del inp
    inp=int(input("number: "))
    if inp==1:
        print_.window6(); #Choose a number
    else:
        print_.window7(); #Voyage; info
        voyage.addInfo()

if inp==3:
    dest=Destination()
    print_.window8()
    dest.addInfo()
