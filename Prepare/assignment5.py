'''Name: Peace Oloruntoba
  Matric No: AUL/SCI/21/00726
  Dept.: Computing'''

import csv

with open('student.csv','w') as f:
    writer =csv.writer(f)
    writer.writerow(["Name","Matric Number","Level","Date Of Birth","State of Origin"])
    for i in range(10):
        name = input('enter name: ')
        matric_no=input(str('enter matric no: '))
        level=input(str('enter level: '))
        dob=input(str('date of birth: '))
        sor=input(str('state of origin: '))
        writer.writerow([name,matric_no,level,dob,sor])
        