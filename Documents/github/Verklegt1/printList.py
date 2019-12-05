from getStaff1_4 import staffInfo
from leitaVoyage import*

def printList(userInput):

    #toPrint = staffInfo(userInput)
    #toPrint = leitaVoyage()

    for i in range(len(toPrint)):
        for j in range(len(toPrint[0])-1):
            print(toPrint[i][j] + ','),
        print(toPrint[i][j+1])

printList(3)
