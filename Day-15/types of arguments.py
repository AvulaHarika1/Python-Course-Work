'''
1.position
2.keyword
3.default
4.variable len
'''
'''#position
def display(name,email,pwd):
    print("Name:",name)
    print("Email:",name)
    print("password:",name)
display('harika','harikaavula76@gmail.com','hari@123')
display('subha','subhamovva76@gmail.com','subha@123')
display('maha','mahakarncharlapalli76@gmail.com','maha@123')'''

'''
#keyword
def display(name,email,pwd):
    print("Name:",name)
    print("Email:",email)
    print("password:",pwd)
display(name='harika',email='harikaavula76@gmail.com',pwd='hari@123')
display(name='subha',email='subhamovva76@gmail.com',pwd='subha@123')
display(name='maha',email='mahakarncharlapalli76@gmail.com',pwd='maha@123')'''

#default
'''
def display(name,email,pwd):
    print("Name:",name)
    print("Email:",email)
    print("password:",pwd)
display('harika','harikaavula76@gmail.com','hari@123')
display('harika','harikaavula76@gmail.com','hari@123')'''

'''#variable len
def display(*names):
    print("Name:",names)
display('harika','subha','maha','gaya','sandy','dhanu')
display('harika','subha','sandy','dhanu')
display('harika','subha','dhanu')
display('harika','dhanu')'''

def display(**names):
    print("Names:",names)
display(k1='harika',k2='subha',k3='maha',k4='gaya',k5='sandy',k6='dhanu')
display(k1='harika',k2='subha',k3='sandy',k4='dhanu')
display(k1='harika',k2='subha',k3='dhanu')
display(k1='harika',k2='dhanu')
