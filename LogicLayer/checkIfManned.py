import csv
from LogicLayer.Date import*

def checkIfManned(voyage):

    flNo = voyage.flightNumber

    day = str(voyage.departure[0:2])
    month = str(voyage.departure[3:5])
    year = str(voyage.departure[6:10])

    standardDate = year + '-'+ month + '-' + day + 'T' + '00:00:00'

    today=now()

    path = '/Users/hildur/Documents/github/verklegt_namskeid_1/csvFiles/'

    if today>standardDate:
        file=path+'PastFlights.csv'
    else:
        file=path+'UpcomingFlights.csv'


    captain_bool = 0
    copilot_bool = 0
    fsm_bool = 0

    with open(file,'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if row['flightNumber'] == flNo:
                if 'captain' in row:
                    if row['captain'] is not None:
                        captain_bool = 1
                if 'copilot' in row:
                    if row['copilot'] is not None:
                        copilot_bool = 1
                if 'fsm' in row:
                    if row['fsm'] is not None:
                        fsm_bool = 1

    return captain_bool, copilot_bool, fsm_bool
