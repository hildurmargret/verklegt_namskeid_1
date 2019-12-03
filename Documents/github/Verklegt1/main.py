#!/usr/bin/env python3
from pagePrints import*
from Staff import*
from Voyage import*
from Destination import*
from Airplane import*
from Windows import*
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=40, cols=100))

print_=pagePrints(100,40)
print_.frontPage() #'c', 'g', 'u'

windows=Windows()
windows.mainMenu()
