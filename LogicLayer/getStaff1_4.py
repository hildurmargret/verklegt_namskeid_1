import csv
from LogicLayer.leitaStaff import *
from ModelClasses.Staff import *

# def staffInfo(input_num, input_string):
#
#     path='/Users/valdisbaerings/Documents/github/verklegt_namskeid_1/csvFiles/'
#     skra='Crew.csv'
#
#     file=path+skra
# 
#     ssn=[]
#     rank=[]
#
#     employees = []
#
#     with open(file,'r') as csv_file:
#         csv_reader = csv.DictReader(csv_file)
#         for row in csv_reader:
#             if input_num==1:
#
#                 empl = createStaff(row['name'],row['ssn'],row['address'],row['phonenumber'],'email',row['rank'],row['role'],row['licence'])
#                 employees.append(empl)
#
#             elif input_num==2:
#                 if row['role']=='Pilot':
#                     empl = createStaff(row['name'],row['ssn'],row['address'],row['phonenumber'],'email',row['rank'],row['role'],row['licence'])
#                     employees.append(empl)
#
#             elif input_num==3:
#                 if row['licence'] == 'N/A':
#                      empl = createStaff(row['name'],row['ssn'],row['address'],row['phonenumber'],'email',row['rank'],row['role'],row['licence'])
#                      employees.append(empl)
#
#             elif input_num==4:
#
#                 ssn,rank=leitaStaff(input_string,file,ssn,rank)
#                 for i in range(len(ssn)):
#                     if row['ssn']==ssn[i]:
#                         empl = createStaff(row['name'],row['ssn'],row['address'],row['phonenumber'],'email',row['rank'],row['role'],row['licence'])
#                         employees.append(empl)
#                         break
#     return employees
