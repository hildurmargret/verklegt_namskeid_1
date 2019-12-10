def emplFromList(employees):
    for i in range(len(employees)):
        print(i+1,end="")
        if employees[i].licence == 'N/A':
            print(" " + employees[i].name + ', ' + employees[i].SSN + ', ' + employees[i].address + ', ' + employees[i].phoneNumber + ', ' + employees[i].role + ', ' + employees[i].rank)
        else:
            print(" " + employees[i].name + ', ' + employees[i].SSN + ', ' + employees[i].address + ', ' + employees[i].phoneNumber + ', ' + employees[i].role + ', ' + employees[i].rank + ', ' + employees[i].licence)
    inp=int(input("Number: "))
    employee=employees[inp-1]
    return employee

def cabinFromList(employees):
    counter=0
    for i in range(len(employees)):
        if employees[i].licence == 'N/A':
            print(counter+1,end="")
            counter+=counter+1
            print(" " + employees[i].name + ', ' + employees[i].SSN + ', ' + employees[i].address + ', ' + employees[i].phoneNumber + ', ' + employees[i].role + ', ' + employees[i].rank)
    inp=int(input("Number: "))
    employee=employees[inp-1]
    return employee

def pilotsFromList(employees):
    counter=0
    for i in range(len(employees)):
        if employees[i].licence != 'N/A':
            print(counter+1,end="")
            counter=counter+1
            print(" " + employees[i].name + ', ' + employees[i].SSN + ', ' + employees[i].address + ', ' + employees[i].phoneNumber + ', ' + employees[i].role + ', ' + employees[i].rank + ', ' + employees[i].licence)
    inp=int(input("Number: "))
    employee=employees[inp-1]
    return employee
