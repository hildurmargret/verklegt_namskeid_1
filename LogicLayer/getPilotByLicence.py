from getPilotsByAirplanes import*
def pilotsByLicence():
    inp="NAFokkerF100"
    line=[]
    dict=pilotsByAirplanes()
    for key in dict:
        if key==inp:
            end=(len(dict[key]))
            for i in range(0,end):
                line.append(dict[key][i])


    print(inp)
    end=len(line)
    for i in range(0,end,2):
        print(line[i] + " " + line[i+1])
    print("")
