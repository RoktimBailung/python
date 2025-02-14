# FACTORIAL PROBLEM

num=int(input("Enter a number \n"))
fact=1
nnum=num
if(num>=0):
    if(num==0):
        print("Factorial of 0 is",fact)
    else:
        while(num != 1):
            fact*=num
            num-=1
            print("Factorial of ",nnum,"is",fact)
else:
    print("Invalid")

# FINDING THE NUMBER OF DIGITS IN A NUMBER

num=abs(int(input("Ente a number \n")))
num1=num
count=1
while(num>9):
    num=num//10
    count+=1

print("The number of digit in",num1,"is",count)

# REVERSING A DIGIT

num=int(input("Enter a number: \n"))
absnum=abs(num)
rev=absnum%10
absnum=absnum//10
while(absnum>0):
    r=absnum%10
    absnum=absnum//10
    rev=rev*10+r
if(num>=0):
    print("The reverse of the given number is:",rev)
else:
    rev=rev-2*rev
    print("The reverse of the given digit is:",rev)
    
# # FOR PALINDROME JUST CHECK A CASE GIVEN BELOW

if(num==rev):
    print("palindrome")
else:
    print("Not palindrome")
