from getStaff1_4 import staffInfo

def printList(userInput):

    toPrint = staffInfo(userInput)

    for i in range(len(toPrint)):
        for j in range(len(toPrint[0])-1):
            print(toPrint[i][j] + ','),
        print(toPrint[i][j+1])

printList(4)
