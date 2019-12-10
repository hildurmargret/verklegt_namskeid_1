def emplFromList(employee):
    for i in range(len(employees)):
        print(i+1,end="")
        print(" " + employees[i].name)
    inp=int(input("Number: "))
    employee=employees[inp-1]
    return employee
