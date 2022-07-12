a=int(input("enter the number "))
s=0
while a>0:
    d=a%10
    s=s+d
    a=a/10

print(int(s))