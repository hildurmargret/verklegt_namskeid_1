import csv
from LogicLayer.Date import*
from ModelClasses.flightRoute import*
from DataLayer.OpenFile import*
from DataLayer.read_pastFlights import*

def employeeOccupied(employee,voyage):

    today=now()

    if today>voyage.departureFlight.departure:
        file='PastFlights copy.csv'
    else:
        file='UpcomingFlights copy3.csv'

    flights = read_pastFlights(file)

    voyYear = int(voyage.departureFlight.departure[0:4])
    voyMonth = int(voyage.departureFlight.departure[5:7])
    voyDay = int(voyage.departureFlight.departure[8:10])

    voyDate = getDate(voyYear,voyMonth,voyDay,0,0)

    for flight in flights:
        flYear = int(flight.departure[0:4])
        flMonth = int(flight.departure[5:7])
        flDay = int(flight.departure[8:10])

        flDate = getDate(flYear,flMonth,flDay,0,0)

        if voyDate==flDate:
            if employee.SSN==flight.captain:
                return True
            if employee.SSN==flight.copilot:
                return True
            if employee.SSN==flight.fsm:
                return True
            if employee.SSN==flight.fa1:
                return True
            if employee.SSN==flight.fa2:
                return True
    return False
