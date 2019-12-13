from LogicLayer.leitaStaff import*
from UILayer.UI_Manager import*
from UILayer.chooseEmplFromList import*
from DataLayer.employeeOccupied import*
def UIappointEmptoVoy(voyage):
    UI = UI_Manager()

    insignia = voyage.departureFlight.aircraftId
    airplanes = UI.UIgettingAirplanes()
    planeid = ''

    for plane in airplanes:
        if plane.planeInsignia == insignia:
            planeid = plane.planeTypeId


    if voyage.departureFlight.captain != '':
        print("There's already a captain assigned to this voyage")
        change = int(input('Choose a different captain? [1: yes, 0: no] '))
    else:
        change = 1

    if change:
        valid_captain = 0
        while not valid_captain:
            print('Choosing captain')
            captain = input('Name or ssn: ')
            if captain == 'CANCEL':
                valid_captain = 1
                return 0
            elif captain != '':
                employees = UI.UIgetEmployees(captain)
                employee=emplFromList(employees)

                if employee != 0:
                    if employee.rank != 'Captain':
                        print(employee.name + ' is not a captain. Please choose an employee with the appropriate rank')
                    elif employee.licence != planeid and planeid != '':
                        print(employee.name + ' does not have the required licence.')
                        print('Licence needed: '+planeid)
                    else:
                        if employeeOccupied(employee,voyage):
                            print(employee.name + ' is not available for this flight. Please choose another employee')
                        else:
                            valid_captain=1
                            voyage.departureFlight.captain = employee.SSN
                            voyage.returnFlight.captain = employee.SSN


    if voyage.departureFlight.copilot != '':
        print("There's already a copliot assigned to this voyage")
        change = int(input('Choose a different copliot? [1: yes, 0: no] '))
    else:
        change = 1

    if change:
        valid_copilot = 0
        while not valid_copilot:
            print('Choosing copilot')
            copilot = input('Name or ssn: ')
            if copilot == 'CANCEL':
                valid_copilot = 1
                return 0
            else:
                employees = UI.UIgetEmployees(copilot)
                employee=emplFromList(employees)

            if employee != 0:
                if employee.rank != 'Copilot':
                    print(employee.name + ' is not a copilot. Please choose an employee with the appropriate rank')
                elif employee.licence != planeid and planeid != '':
                    print(employee.name + ' does not have the required licence.')
                    print('Licence needed: '+planeid)
                else:
                    if employeeOccupied(employee,voyage):
                        print(employee.name + ' is not available for this flight. Please choose another employee')
                    else:
                        valid_copilot=1
                        voyage.departureFlight.copilot = employee.SSN
                        voyage.returnFlight.copilot = employee.SSN


    if voyage.departureFlight.fsm != '':
        print("There's already a flight service manager assigned to this voyage")
        change = int(input('Choose a different flight service manager? [1: yes, 0: no] '))
    else:
        change = 1

    if change:
        valid_fsm = 0
        while not valid_fsm:
            print('Choosing flight service manager')
            fsm = input('Name or ssn: ')
            if fsm == 'CANCEL':
                valid_fsm = 1
                return 0
            else:
                employees = UI.UIgetEmployees(fsm)
                employee=emplFromList(employees)

            if employee != 0:
                if employee.rank != 'Flight Service Manager':
                    print(employee.name + ' is not a flight service manager. Please choose an employee with the appropriate rank')
                else:
                    if employeeOccupied(employee,voyage):
                        print(employee.name + ' is not available for this flight. Please choose another employee')
                    else:
                        valid_fsm=1
                        voyage.departureFlight.fsm = employee.SSN
                        voyage.returnFlight.fsm = employee.SSN


    add = 0
    addTwo = 0
    if voyage.departureFlight.fa1 != '' and voyage.departureFlight.fa2 != '':
        print("There are already two flight attendants assigned to this voyage")
    elif voyage.departureFlight.fa1 != '' or voyage.departureFlight.fa2 != '':
        print("There's one flight attendant assigned to this voyage")
        add = int(input('Add flight attendant? [1: yes, 0: no] '))
    else:
        addTwo = 1

    if addTwo or (add and voyage.departureFlight.fa1 == ''):
        valid_fa1 = 0
        while not valid_fa1:
            print('Adding a flight attendant')
            fa1 = input('Name or ssn: ')
            if fa1 == 'CANCEL':
                valid_fa1 = 1
                return 0
            else:
                employees = UI.UIgetEmployees(fa1)
                employee=emplFromList(employees)

            if employee != 0:

                if employee.rank != 'Flight Attendant':
                    print(employee.name + ' is not a flight attendant. Please choose an employee with the appropriate rank')
                else:
                    if employeeOccupied(employee,voyage):
                        print(employee.name + ' is not available for this flight. Please choose another employee')
                    else:
                        valid_fa1=1
                        voyage.departureFlight.fa1 = employee.SSN
                        voyage.returnFlight.fa1 = employee.SSN

    if addTwo or (add and voyage.departureFlight.fa2 == ''):
        valid_fa2 = 0
        while not valid_fa2:
            print('Adding a flight attendant')
            fa2 = input('Name or ssn: ')
            if fa2 == 'CANCEL':
                valid_fa2 = 1
                return 0
            else:
                employees = UI.UIgetEmployees(fa2)
                employee=emplFromList(employees)
            if employee != 0:
                if employee.rank != 'Flight Attendant':
                    print(employee.name + ' is not a flight attendant. Please choose an employee with the appropriate rank')
                else:
                    if employeeOccupied(employee,voyage):
                        print(employee.name + ' is not available for this flight. Please choose another employee')
                    else:
                        valid_fa2=1
                        voyage.departureFlight.fa2 = employee.SSN
                        voyage.returnFlight.fa2 = employee.SSN

    return voyage
