'''#local scope
def display():
    n=10
    print("Inside:",n)
display()
print("Outside:",n)
#error vasthundhi...'''

'''
def display():
    n=10
    print("Inside:",n)
display()'''

'''
n=10
def display():
    print("Inside:",n)
display()
print("Outside:",n)'''


#global n(inside lo vunna var outside lo kuda print chesthaki use chestham)
'''def display():
    global n
    n=10
    print("Inside:",n)
display()
print("Outside:",n)'''
'''
def display(n):
    #global n
    n+=10
    print("Inside:",n)
n=10
display()
print("Outside:",n)'''

'''
def display(n):
    global n
    n+=10
    print("Inside:",n)
n=10
display()
print("Outside:",n)'''



#non local
'''
def outer():
    n=10
    def inner():
        nonlocal n
        n+=10
        print("Inner function:",n)
    inner()
    print("Outer function:",n)
outer()'''

#examples
'''s='python'
print(len(s))
len=5
print(len(s))'''




