# if statement
print('Enter your GPA')
gpa=float(input())
if (gpa>8.5):
  print('You are a top student,and are eligible for scholarship')
else:
  print('You are not a top student, and not eligible for scholarship')

print('Have a nice day')

# PROBLEM 1 checking even and odd number
print('Enter the number')
num=int(input())
if(num%2==0):
  print('The number entered is Even')
else:
  print('The number entered is Odd')

# PROBLEM 2 checking the lastdigit.
print('Enter the number')
num=int(input())
if(num%5==0):
  if(num%10==0):
    print('0')
  else:
    print(5)
else:
     print('other')

# PROBLEM 3 Ranking problem on the basis of marks
marks=int(input('Enter your marks:'))
if marks>=0 and marks<=100:
  if marks>=90:
    print('A')
  elif marks>=80:
    print('B')
  elif marks>=70:
    print('C')
  elif marks>=60:
    print('D')
  else:
    print('E')
else:
  print('Invalid input')

# PROBLEM 4

print('Travel from City A to City B')
time=int(input('Enter time in hrs \n'))

longer=int(input('Define Longer in hrs \n'))
if(time>=longer):
  price=int(input('Enter the price in ruppees \n'))
  higher=int(input('Define Higher in ruppees \n'))
  if(price>=higher):
    print('Train')
  else:
    print('Coach')
else:
  price=int(input('Enter the price in ruppees \n'))
  higher=int(input('Define Higher in ruppees \n'))
  if(price>=higher):
    print('Daytime flight')
  else:
    print('Red eye flight')

print('Arrive in City B')
