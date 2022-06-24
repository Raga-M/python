#a=[8,10,8,2,4,1,20,30,40,55,43,56,67,99,100,1111]
a=[]
for i in range(6):
    n=int(input())
    a.append(n)
n=len(a)-1
for i in range(0,n):
    for j in range (0,n):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
    n=n-1
print((a))


