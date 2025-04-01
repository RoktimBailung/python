# Iterators
c=["rcb","csk","mi","lsg"]
iterator=iter(c)
print(next(iterator))
print(next(iterator))
Controlled one by one iterations through a list of elements

# generator
def count(n):
    count1=1
    while count1<n:
        yield count1
        count1+=1
gen=count(5)
print(next(gen))
print(next(gen))

# lambda functions
add=lambda x,y: x+y
sub=lambda x,y: x-y

print(add(10,20))
print(sub(100,20))

# enumerate functions

ipl=["rcb","csk","lsg","mi","dc","gt"]
for x in enumerate(ipl):
    print(x)

# zip function

ipl=["rcb","csk","lsg","mi","dc","gt"]
trophies=[0,6,0,6,0,1]
print(list(zip(ipl,trophies)))
print(dict(zip(ipl,trophies)))

# mapping functions

a=[10,20,30,40,50]
b=[1,2,3,4,5]
def sub(x,y):
    return x-y
s=map(sub,a,b)
print(list(s))

# filter functions
import math
a=[10,20,-30,40,-50]

def square_root(x):
    return math.sqrt(x)
def is_positive(x):
    if x>=0:
        return x

s=map(square_root,filter(is_positive,a))
print(type(s))
print(list(s))
