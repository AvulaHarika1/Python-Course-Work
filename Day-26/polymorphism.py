





































































































































#polymorphism
#same mthd diff parameters-mthd overloading
#same mthd same paRAMETERS one is for parent class and one is for child class
'''

class Hotstar:
    def __init__(self,name):
        self.name=name
        print(f'hi{self.name},welcome to the hotstar')
    def login(self):
         print("You can login")
    def dashboard(self):
        print("You can see the dashboard items")
    def search(self):
        print("You can search")
    def languages(self):
        print("You select the languages")
    def playcontrollers(self):
        print("You can pause and paly the video")
    def ads(self):
         print("ads will run")
    def movies(self):
         print("You can limited access for movies")
    def sports(self):
        print("limited time you can watch sports")
    def quality(self):
         print("limited quality")
            
harika=Hotstar('harika')
harika.login()
harika.dashboard()
harika.search()
harika.languages()
harika.playcontrollers()
harika.ads()
harika.movies()
harika.sports()
harika.quality()
'''

#mthd overriding
'''
class premiumHotstar:
    def __init__(self,name):
        self.name=name
        print(f'hi{self.name},welcome to the premium hotstar')
    def ads(self):
         print("ads won't run")
    def movies(self):
         print("You can unlimited access for movies")
    def sports(self):
        print(" you can watch sports")
    def quality(self):
         print("high quality")
        
subha=premiumHotstar('subha')
subha.login()
subha.dashboard()
subha.search()
subha.languages()
subha.playcontrollers()
subha.ads()
subha.movies()
subha.sports()
subha.quality()
'''

#operatot overloading
'''
class Number:
    def __init__(self,n):
        self.n=n
    def __add__(self,other):
        return self.n+other.n
    def __sub__(self,other):
        return self.n-other.n
    def __mul__(self,other):
        return self.n*other.n
    def __truediv__(self,other):
        return self.n/other.n
    def __eq__(self,other):
        return self.n==other.n
    def __lt__(self,other):
        return self.n>other.n
    def __gt__(self,other):
        return self.n<other.n
    def __str__(self):
        return str(self.n)
n1=Number(10)
n2=Number(20)
print(n1+n2)
print(n1-n2)
print(n1*n2)
print(n1/n2)
print(n1==n2)
print(n1<n2)
print(n1>n2)
print(n1,n2)
'''



