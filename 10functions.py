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

# functions examples
# Q1 To calculate the number of uppercase,lowercase,charcaters,words of the sentence
def cupper(s):
    upperl=0
    for c in s:
        if(c.isupper()):
            upperl+=1
    return upperl

def clower(s):
    lowerl=0
    for c in s:
        if(c.islower()):
            lowerl+=1
    return lowerl

def ccharacter(s):
    ccount=0
    for c in s:
        ccount+=1
    return ccount

def cwords(s):
    count=0
    for c in s:
        if(c==' '):
            count+=1
    return count+1

sentence=input("Enter a Sentence\t")
print(f'The number of upper case letter ={cupper(sentence)}')
print(f'The number of lower case letter ={clower(sentence)}')
print(f'The number of total character ={ccharacter(sentence)}')
print(f'The number of words ={cwords(sentence)}')


# Q2 To calculate the area and perimeter of the circle and rectangle using functions
def carea(r):
    a=3.14*r*r
    return round(a)
def rarea(l,b):
    a=l*b
    return round(a)
def cperi(r):
    p=2*3.14*r
    return round(p)
def rperi(l,b):
    p=2*(l+b)
    return round(p)

shape=input("Enter the shape either circle or rectangle :\t")
if(shape=="circle"):
    prop=input("Enter either area or perimeter : \t")
    rad=int(input("Enter the radius of the circle: \t"))
    if (prop=="area"):
        print(f'The area of the circle is={carea(rad)}')
    elif (prop=="perimeter"):
        print(f'The perimeter of the circle is={cperi(rad)}')
    else:
        print("invalid")
elif(shape=="rectangle"):
    prop=input("Enter either area or perimeter : \t")
    l=int(input("Enter the length  of the rectangle: \t"))
    b=int(input("Enter the  breadth of the rectangle: \t"))
    if (prop=="area"):
        print(f'The area of the rectangle is={rarea(l,b)}')
    elif (prop=="perimeter"):
        print(f'The perimeter of the rectangle is={rperi(l,b)}')
    else:
        print("invalid")
else:
    print("Invalid")

# Q3 To check whether the given points form a triangle or not
def istriangle(x1,y1,x2,y2,x3,y3):
    area=0.5*abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))
    if(area==0):
        print("Not a triangle")
    else:
        print("It's a triangle")

x1=float(input("Enter the x coordinate of 1st point = "))
y1=float(input("Enter the y coordinate of 1st point = "))
x2=float(input("\nEnter the x coordinate of 2nd point = "))
y2=float(input("Enter the y coordinate of 2nd point = "))
x3=float(input("\nEnter the x coordinate of 3rd point = "))
y3=float(input("Enter the y coordinate of 3rd point = "))
istriangle(x1,y1,x2,y2,x3,y3)
