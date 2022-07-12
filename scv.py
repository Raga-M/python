import csv
with open("t.csv","w") as f:
    w=csv.writer(f)
    w.writerow(["TNO","TraineeName","Qualification"])
    no = int(input ("ente the no. of trainee"))
    for trainee in range(no):
        tno=int(input("enter the id "))
        tname=input("enter the name ")
        tqual=input("enter the qualifcation ")
        w.writerow([tno,tname,tqual])