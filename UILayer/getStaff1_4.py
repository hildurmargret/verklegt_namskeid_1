import csv
from LogicLayer.leitaStaff import *
from ModelClasses.Staff import *

# def staffInfo(input_num, input_string):
#
#     path='/Users/palinakroyer/github/verklegt_namskeid_1/csvFiles/'
#     skra='Crew.csv'
#
#
#     file=path+skra
#
#     ssn=[]
#     rank=[]
#     #employees = {'ssn':[], 'name':[], 'role':[], 'rank':[], 'licence':[], 'address':[], 'phonenumber':[]}
#     employees = []
#
#     with open(file,'r') as csv_file:
#         csv_reader = csv.DictReader(csv_file)
#         for row in csv_reader:
#             if input_num==1:
#                 #employees['ssn'].append(row['ssn'])
#                 #employees['name'].append(row['name'])
#                 #employees['role'].append(row['role'])
#                 #employees['rank'].append(row['rank'])
#                 #employees['licence'].append(row['licence'])
#                 #employees['address'].append(row['address'])
#                 #employees['phonenumber'].append(row['phonenumber'])
#
#                 if row['licence'] == 'N/A':
#                     empl = createCabin(row['name'],row['ssn'],row['address'],row['phonenumber'],'email',row['rank'],row['role'])
#                     employees.append(empl)
#                 else:
#                     empl = createPilot(row['name'],row['ssn'],row['address'],row['phonenumber'],'email',row['rank'],row['role'],row['licence'])
#                     employees.append(empl)
#
#             elif input_num==2:
#                 if row['role']=='Pilot':
#                     empl = createPilot(row['name'],row['ssn'],row['address'],row['phonenumber'],'email',row['rank'],row['role'],row['licence'])
#                     employees.append(empl)
#
#             elif input_num==3:
#                  empl = createCabin(row['name'],row['ssn'],row['address'],row['phonenumber'],'email',row['rank'],row['role'])
#                  employees.append(empl)
#
#             elif input_num==4:
#                 #inpt=input('Please enter the name or SSN of employee')
#                 ssn,rank=leitaStaff(input_string,file,ssn,rank)
#                 for i in range(len(ssn)):
#                     if row['ssn']==ssn[i]:
#                         if row['licence'] == 'N/A':
#                             empl = createCabin(row['name'],row['ssn'],row['address'],row['phonenumber'],'email',row['rank'],row['role'])
#                             employees.append(empl)
#                         else:
#                             empl = createPilot(row['name'],row['ssn'],row['address'],row['phonenumber'],'email',row['rank'],row['role'],row['licence'])
#                             employees.append(empl)
#                         break
#     return employees

#empl = staffInfo(1)

#for i in range(len(empl)):
    #print(empl[i].name)

#end=len(empl['name'])

#for i in range(0,end):
#    for key in empl:
#        print(empl[key][i])
#    print
