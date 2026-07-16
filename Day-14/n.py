
#nletter
'''n=int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==j:
            print("*" ,end=" ")
        else:
            print(" " ,end=" ")
    print()
'''
#cletter
'''
n=int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0  :
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()'''

#bletter
'''
n=int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1 or i == n//2 :
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()'''

#dletter
'''
n = int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()'''

#e letter
'''
n=int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or i==n//2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()'''
#f letter
'''n=int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i==n//2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()'''
#hlter
'''n=int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        if  j == 0 or j==n-1 or i==n//2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()'''
#i letter
'''
n=int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        if  i == 0 or i==n-1 or j==n//2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()'''
#k letter
'''
 n=int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        if j==0 or (j==4 and i==0) or (j==3 and i==1) or (j==4 and i==4) or (i==2 and j<3) or (i==3 and j==3):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()'''
#p letter
'''
n=int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        if j==0 or j==0 or i==0 or i==n//2 or (j==n-1 and i<n//2):
            print("*", end=" ")
        else:
            print(" ", end=" ")'''
    print()
