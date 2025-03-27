# FUNCTIONS

# Function to perform some arithmetic functions
def add(a,b):
    return a+b
def sub(m,n):
    return m-n
def mul(h,k):
    return h*k
def div(g,k):
    return g/k

print("What Arithmetic Operation You would like to perform. Type \n 1 for addition \n 2 for subtraction\n 3 for multiplication\n 4 for division\n")
s=int(input("Ente your choice \t"))
if (s==1):
    a1=int(input("Enter the 1st number to be added \t"))
    b1=int(input("Enter the 2nd number to be added \t"))
    print("Additioin of the given number",a1,b1,"is =",add(a1,b1))
elif (s==2):
    a2=int(input("Enter the 1st number to be subtracted\t"))
    b2=int(input("Enter the 2nd number to be subtracted \t"))
    print("Subtraction of the given number",a2,b2,"is =",sub(a2,b2)) 
elif (s==3):
    a3=int(input("Enter the 1st number to be multiplied"))
    b3=int(input("Enter the 2nd number to be multiplied \t"))
    print("multiplication of the given number",a3,b3,"is =",mul(a3,b3))
else:
    a4=int(input("Enter the 1st number to be divided\t"))
    b4=int(input("Enter the 2nd number to be divided \t"))
    print("Division of the given number",a4,b4,"is =",div(a4,b4))

# Function to display the total cost after applying a certain discount 

def discount(cost,dis):
    total_money=cost-(cost*dis/100)
    return total_money
amount=float(input("Enter the bill amount \t"))
d=float(input("Enter the discount percentage \t"))
print("The Total Balance to be paid is =",discount(amount,d))

#  functions to find the minimum  and maximum from a list

def l_min(l):
    min1=l[0]
    for i in range(len(l)):
        if (l[i]<min1):
            min1=l[i]
    return min1

def l_max(l):
    max1=l[0]
    for i in range(len(l)):
        if (l[i]>max1):
            max1=l[i]
    return max1

def l_append_before(l,z):
    newl=[]
    for i in range(len(z)):
        newl.append(z[i])
    for i in range(len(l)):
        newl.append(l[i])
    return newl

def l_append_end(l,z):
    newl=[]
    for i in range(len(l)):
        newl.append(l[i])
    for i in range(len(z)):
        newl.append(z[i])
    return newl

def l_average(l):
    sum=0
    for i in range(len(l)):
        sum=sum+l[i]
    avg=sum/len(l)
    return avg

x=[]
y=[1,2,3]
i=1
while(i!=0):
    x1=int(input("Enter the element of the list \t"))
    x.append(x1)
    i=int(input("Enter '0' to stop and '1' to continue entering on list l \t"))

print("The list l=",x)
print("\n The minimum element in the list is ",l_min(x))
print("\n The maximum element in the list is ",l_max(x))
print("\n newlist after list y is append befoe list l is =",l_append_before(x,y))
print("\n newlist after list y is append at end of the list l is =",l_append_end(x,y))
print("\n The Average of the list l is =", l_average(x))

# ovbious sort 
def sort(l):
    nlist=[]
    while(len(l)>0):
        mini=l[0]
        for i in range(len(l)):
            if l[i]<mini:
                mini=l[i]
        nlist.append(mini)
        l.remove(mini)
    return nlist
    
n=int(input("Enter the number of elements you required in the list \t"))
l1=[]
for i in range(n):
    l1.append(int(input("Enter the element")))
print("After sorting the list :",sort(l1))

