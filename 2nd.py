# Using Basic Print and Input command to take input from User and Displaying some Results
print("Type your name")
n= str(input())
print("Type your location")
p= str(input())
print(" hello ", n, " how is the weather in",p,"?")
age= int(input("What is your age?"))
print("Good to know that you are",age,"years old")

# Calculating Area of Different Geometrical shapes
# Calculating area pf circles
rad=int(input("enter the radius of the circle"))
area=3.14*rad*rad
print("area of the circle with radius",rad,"is",area)

# Calculating area of rectangle
l=float(input("Enter the length \n"))
b=float(input("Enter the breadth \n"))
area1=l*b
print("The area of the Rectangle is",area1)

# Calculating area of Trapezium
h=int(input("Enter the height \n"))
b=int(input("Enter the base \n"))
area3=0.5*(b+b)*h
print(f'The area of Trapezium is {area3}')

