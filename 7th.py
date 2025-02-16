# USING OF FOR LOOP
#SUM OF FIRST 10 INTEGERS

sum=0
for i in range(10):
    sum+=i
print("sum=",sum)

# MULTIPLICATION TABLE GENERATOR
num=int(input("Enter the number: \t"))
for i in range(1,11):
    print(num," X ",i,'=',num*i

# USE OF FOR LOOP IN DIFFERENT WAYS
Will print all the odd numbers between 1 and 10
for x in range(1,10,2):
    print(x)

# Will print all the numbers between 9 and 0 in renerse order
for x in range(10,-1,-1):
    print(x)

# For loop without the use of range
name="Roktim"
for letter in name:
    print(letter)
  
# USE OF NESTED FOR LOOP

count=0
for i in range(11):
    for j in range(5):
        print(i,j,i*j)
        count+=1
print(f'The number of times the loops get executed is = {count}')

# NESTED LOOP APPLICATION
1. TO PRINT PRIME NUMBERS LESS THAN THE GIVEN NUMBER
num=int(input("Enter the number \n"))
if num>2:
    print(2,' ')
for i in range(3,num):
    flag=False
    for j in range(2,i):
        if i%j==0:
            flag=False
            break
        else:
            flag=True
        if (flag):
            print(i,end=' ')
          
# PROGRAM TO SHOW TOTAL TRADE VALUE OF TRADERS

empId=input("ENter the EMployee Id \t")
while(empId != '-1'):
    trade=int(input("ENter the trade amount\t"))
    profit_loss=0
    while(trade!=0):
        profit_loss+=trade
        trade=int(input("Enter your Trade Amount \t"))
    print(f'The total amount of trade for {empId} is {profit_loss}')
    empId=input("ENter the Employee Id\t")

# PRINTING THE NUMBER OF CHARACTERS OF THE LONGEST WORD ENTERED(NOT COMPLETED)
  
word=input("Enter your word, press -1 to terminate \t")
max=0
l1=len(word)
while (word!='-1'):
    if l1>max:
        word=input("Enter your word, press -1 to terminate \t")
        l2=len(word)
    if (l2>l1):
        max=l2

print(l1)
