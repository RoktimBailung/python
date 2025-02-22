# Dot product
x=[1,2,3]
y=[2,3,4]
dot_prof=(1*2)+(2*3)+(3*4)
print(dot_prof)

# general approach of dot product
x=[1,2,3]
y=[3,2,1]
prod=0
for i in range(len(x)):
    prod=prod+x[i]*y[i]
print(f'The Dot Product is={prod}')

# addition of two matrices
x=[[1,2,3],[4,5,6],[7,8,9]]
y=[[9,8,7],[6,5,4],[3,2,1]]
sum=[[0,0,0],[0,0,0],[0,0,0]]
dim=3
for i in range(dim):
    for j in range(dim):
        sum[i][j]=x[i][j]+y[i][j]
print("Summation of the matrix is =\n",sum)

# Multiplication of the Matrix
x=[[1,2,3],[4,5,6],[7,8,9]]
y=[[9,8,7],[6,5,4],[3,2,1]]
prod=[[0,0,0],[0,0,0],[0,0,0]]
dim=3
for i in range(dim):
    for j in range(dim):
        for k in range(dim):
            prod[i][j]=prod[i][j]+x[i][k]*y[k][j]
print("Product of the matrix is =\n",prod)
