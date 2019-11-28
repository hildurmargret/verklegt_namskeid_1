#!/usr/bin/env python3
from pagePrints import*



print_=pagePrints(80,25)
print_.frontPage()

inp=input()

if inp=="c":

    print_.window1();

input=int(input("number: "))
if input==1:

    from Staff import *
    staff=Staff()
    staff.addInfo()
