# LIST
l=[1,2,3,4,5]
print(l)
l.append(6) 
# append cant take two values at once
print(l)
l.append(6)
print(l)
# Every element in list is unique
m=[]
m.append(l)
print("list m=",m) 
# appending list l in m
m.append([2,3,4,5])
print("appending two list under one list =",m)
# two dimension
print(m[0][0])

# BIRTHDAY PARADOX
import random
l=[]
for i in range(100):
    l.append(random.randint(1,365))
l.sort()
print(l)
i=0
flag=0
while(i<len(l)-2):
    if(l[i]==l[i+1]==l[i+2]):
        print("Repeats",l[i],l[i+1],l[i+2])
        flag=1
    i+=1
    if(l[i]==l[i+1]):
        print("Repeats",l[i],l[i+1])
        flag=1
    i+=1
if(flag==0):
    print("No repeatition")
