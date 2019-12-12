from ModelClasses.Staff import*
from ModelClasses.Airplane import*
from LogicLayer.Date import*
from DataLayer.getDestinations import*
from DataLayer.getAircraft import*
class Inp3():

    def addRouteInp(self,voyage):
        destinations = getDestinations()
        aircraft = list_all_aircraft()
        self.flightNumber = voyage.flightNumber

        validDest_bool = 0
        correctDest_bool=0
        while not validDest_bool:
            self.arrivingAt=input("Destination: ")
            for dest in destinations:
                if self.arrivingAt == dest.id and dest.id != 'KEF':
                    correctDest_bool=1
            if self.arrivingAt=="CANCEL":
                validDest_bool = 1
                return 0
            elif not correctDest_bool:
                print('Invalid input. Destination must be one of the following:')
                for dest in destinations:
                    if dest.id != 'KEF':
                        print(dest.id)
            else:
                validDest_bool = 1

        validDate_bool = 0
        while not validDate_bool:
            date=input("Departure day [dd]: ")
            if date=="CANCEL":
                validDate_bool=1
                return 0
            elif not date.isdigit() or (len(date) != 2):
                print('Invalid input. Departure day must consist of two integers [0-9]')
            elif int(date)<1 or int(date)>31:
                print('Invalid input. Departure day must be in the range 1-31')
            else:
                validDate_bool=1

        validMonth_bool=0
        while not validMonth_bool:
            month=input("Departure month [mm]: ")
            if month=="CANCEL":
                validMonth_bool=1
                return 0
            elif not month.isdigit() or (len(month) != 2):
                print('Invalid input. Departure month must consist of two integers [0-9]')
            elif int(month)<1 or int(month)>12:
                print('Invalid input. Departure month must be in the range 1-12')
            else:
                validMonth_bool=1

        validYear_bool=0
        while not validYear_bool:
            year=input("Departure year [yyyy]: ")
            if year=="CANCEL":
                validYear_bool=1
                return 0
            elif not year.isdigit() or (len(year) != 4):
                print('Invalid input. Departure year must consist of four integers [0-9]')
            elif int(year)<2000 or int(year)>2050:
                print('Invalid input. Departure year must be in the range 2000-2050')
            else:
                validYear_bool=1

        validHour_bool = 0
        while not validHour_bool:
            hour=input("Departure hour [hh]: ")
            if hour=="CANCEL":
                validHour_bool = 1
                return 0
            elif not hour.isdigit() or (len(hour) != 2):
                print('Invalid input. Departure hour must consist of two integers [0-9]')
            elif int(hour)<0 or int(hour)>23:
                print('Invalid input. Departure hour must be in the range 0-23')
            else:
                validHour_bool=1

        validMin_bool = 0
        while not validMin_bool:
            minute=input("Departure minute [mm]: ")
            if minute=="CANCEL":
                validMin_bool = 1
                return 0
            elif not minute.isdigit() or (len(minute) != 2):
                print('Invalid input. Departure minute must consist of two integers [0-9]')
            elif int(minute)<0 or int(minute)>59:
                print('Invalid input. Departure minute must be in the range 0-59')
            else:
                validMin_bool=1

        date=int(date)
        month=int(month)
        year=int(year)
        hour=int(hour)
        minute=int(minute)

        self.departure = getDate(year,month,date,hour,minute)
        self.arrival=add_hour(self.departure,2)

        validAirID_bool = 0
        correctAirID_bool=0
        while not validAirID_bool:
            self.aircraftId=input("Aircraft ID: ")
            for plane in aircraft:
                if self.aircraftId == plane.planeInsignia:
                    correctAirID_bool=1
            if self.aircraftId=="CANCEL":
                validAirID_bool=1
                return 0
            elif not correctAirID_bool:
                print('Invalid input. Aircraft ID must be one of the following:')
                for plane in aircraft:
                    print(plane.planeInsignia)
            else:
                validAirID_bool = 1


        for plane in aircraft:
            if plane.planeInsignia == self.aircraftId:
                capacity = plane.capacity

        validSold_bool=0
        while not validSold_bool:
            self.soldTickets=input("Amount of sold seats: ")
            if self.soldTickets=="CANCEL":
                validSold_bool=1
                return 0
            elif int(self.soldTickets) > int(capacity):
                print('Invalid input. Amount of sold seats exceeds plane capacity')
                print('Airplane capacity: ' + capacity)
            elif int(self.soldTickets) < 0 or self.soldTickets=='':
                print('Please enter an amount in the range 0-' + capacity)
            elif not self.soldTickets.isdigit():
                print('Invalid input. Amount must consist of integers only [0-9]')
            else:
                validSold_bool=1

        return self
