'''
def function_name(arg):
#stmts
return
function_nmae(para)'''

'''
def Wish(name):
    print(f'Welcome to the python course {name}!')
Wish('subbu')
Wish('hari')
Wish('maha')
Wish('subha')'''

'''
def iseven(num):
    if num%2==0:
        return f"{num}-Even number"
    else:
        return f"{num}-odd number"
print(iseven(12))
print(iseven(13))'''



def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    return fact
 num=int(input("Enter the number:"))
 print("Factorial:",factorial(num))

'''
def isprime(num):
    for i in range(2,num//2):
        if num%i==0:
            return f"{num}-Not prime number"
        return f"{num}-Prime Number"
num=int(input("Enter the number:"))
print(isprime(num))'''
