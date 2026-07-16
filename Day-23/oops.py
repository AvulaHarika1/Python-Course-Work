'''
class Flipkart:
    discoumt=10
    products=['laptop','mouse','phone','charger']
    def login(self,username,password):
        self.username=username
        self.password=password
        print(f'welcome to flipkart{self.username}')
harika=Flipkart()
harika.login('harika','harika@123')
dhanu=Flipkart()
dhanu.login('dhanu','dhanu@123')
karthik=Flipkart()
karthik.login('karthik','karthik@123')
'''


'''
class Flipkart:
    discoumt=10
    products=['laptop','mouse','phone','charger']
    @classmethod
    def showproducts(cls):
        print(cls.products)
    def login(self,username,password):
        self.username=username
        self.password=password
        print(f'welcome to flipkart{self.username}')
    @staticmethod
    def banner():
       print("10% discount is going on flipkart,shop now!")
harika=Flipkart()
harika.login('harika','harika@123')
harika.banner()
harika.showproducts()
Flipkart.showproducts()
Flipkart.banner()
'''


#constructor
'''
class Instagram:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        print(f'welcome to flipkart{self.username}')
harika=Instagram('harika','harika@123') '''

class Instagram:
    def __init__(self,username,password):
        self.username=username
        self.__password=password
        self.follwers[]
   def getpasword(self):
       return self.__password
    def getpasword(self,newpassword):
       self.__password=newpassword
harika=Instagram('harika','harika@123')       
print("Before username:"harika.username)
harika.username='dhanu'
print("After username:"harika.username)

print("Before username:"harika.getpassword())
harika.setpassword('dhanu@123')
print("Before username:"harika.getpassword())




