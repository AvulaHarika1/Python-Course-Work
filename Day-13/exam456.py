'''n=int(input("Enter the  size:"))
for row in range(n):
    for sp in range(row):
        print(' ',end=' ')
    for col in range(n-row):
            print('*',end=' ')
    print()
'''




'''
n=int(input("Enter the size:"))
for row in range(n):
    for col in range(n):
        print((row+col)%2,end=' ')
    print()
'''




'''
n=int(input("Enter the size:"))
c=1
for row in range(n):
    for col in range(row):
        print(str(c),end=' ')
        c+=1
    print()'''


n=int(input("Enter the size:"))
c=1
for row in range(n):
    for col in range(row):
        print(str(c).zfill(2),end=' ')
        c+=1
    print()

