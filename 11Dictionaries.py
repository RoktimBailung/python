# Dictionaries
d={}
d['Roktim']=9435715459
d['Anuvab']=6913315033
d['Abhimanyu']=6789564321
print(d)
print("Phone No of Roktim is",d['Roktim'])

# Searching Through a list to fint the max number used using a dictionary
java=['Java', 'is', 'a', 'programming', 'language', 'It', 'is', 'a', 'OOP', 'orineted', 'language','a']
j={}
max=0
s=set(java)
for c in s:
    j[c]=0
for c in java:
    j[c]=j[c]+1
    if (j[c]>max):
        max=j[c]
        ans_word=c
print(j)
print("max=",max)
print("Max word is",ans_word)
