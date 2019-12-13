from DataLayer.OpenFile import *
from DataLayer.read_pastFlights import *
from ModelClasses.flightRoute import *
from LogicLayer.Date import *
from ModelClasses.Voyage import*

def voyageStatus(dep, ret, input_date, input_time):

    inptDay = str(input_date[0:2])
    inptMonth = str(input_date[3:5])
    inptYear = str(input_date[6:10])

    stdInptDate = inptYear + '-' + inptMonth + '-' + inptDay + 'T' + input_time
    #innslegin dagsetning a standard formati

    status=[]
    #fer i gegnum oll dep og ret flug og finn viðeigandi status flugs
    for i in range(len(dep)):
        if dep[i].departure < stdInptDate < dep[i].arrival:
            status.append('In air outbound')
        elif ret[i].departure < stdInptDate < ret[i].arrival:
            status.append('In air homebound')
        elif stdInptDate < ret[i].departure and stdInptDate > dep[i].arrival:
            status.append('On ground at destination')
        elif stdInptDate > ret[i].arrival and stdInptDate > ret[i].departure and stdInptDate > dep[i].arrival and stdInptDate > dep[i].departure:
            status.append('Completed')
        else:
            status.append('Awaiting departure')

    return status #skila streng með status flugs ut
