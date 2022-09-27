def zam(X):
    tmp=X[0]
    X[0]=X[len(X)-1]
A=[]
m=int(input('Enter the length of the array:'))
for i in range(m):
    print('Enter ',i,'element of the array')
    A.append(int(input()))
print(A)
zam(A)
print(A)
