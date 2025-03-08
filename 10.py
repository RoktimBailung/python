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
