# STRINGS OPERATION

a='coffee'
b='bread'
print(a[3:5])
print(b[1:5])
print(a+a[-2::-1])

s='0123456789'
a=s[3]
b=s[5]
print(a+b)

s='0123456789'
a=int(s[3])
b=int(s[5])
print(a+b)

a=98.9
c=round(a)
b=a//1
print(c)

# DYNAMIC TYPING

x,y=12,19
print(x,y)
x,y=y,x
print(x,y)

# USE OF IN OPERATOR
print('roktim' in 'roktim bailung is a good boy')
print('good' in 'hello everyone')

# ESCAPE CHARACTER
print('it's a beautiful day') an error due to same '
correct code
print('It\'s a beautiful day')

# STRING METHODS
x='pytHoN sTrIng mEthOdS'
print(x.lower())
print(x.upper())
print(x.capitalize())
print(x.title())
print(x.swapcase())

x='python dev'
print(x.islower())
print(x.isupper())
print(x.istitle())

y='123'
print(y.isdigit())
print(y.isalpha())

z='asb123'
print(z.isalnum())
a='---python---'
print(a.strip('-'))
print(a.lstrip("_"))
print(a.rstrip('_'))

b='python'
print(b.startswith('p'))
print(b.startswith('P'))
print(b.endswith('n'))
print(b.endswith('N'))

c='python string methods'
print(c.count('t'))
print(c.index('o'))
print(c.replace('s','S'))
