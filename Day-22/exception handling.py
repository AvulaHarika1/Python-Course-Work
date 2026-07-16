'''
try:
    a=int(input("Enter the age: "))
except ValueError:
    print("Enter the age in a digit[0-9] format")
else:
    print("Age:",a)
finally:
    print("ThankYou")
'''

#multiple erros
'''
try:
    #a=int(input("Enter the age: "))
    #print(12/10)
    #print(b)
    #print(13+'14')
    d={1:1,2:2,3:3,4:4,}
    #print(d[5])
    l=[1,2,3]
    #print(1[10])
except ValueError:
    print("EEnter the age in a digit[0-9] format")
except ZeroDivisionError:
    print("cant divide with zero")
except NameError:
    print("define the var")
except TypeError:
    print("Add the same data types")
except KeyError:
    print("Key is not present")
except IndexError:
     print("Index is out of range")
else:
    print("Age:",a)
finally:
    print("ThankYou")
'''

'''
try:
    a=int(input("Enter the age: "))
    #print(12/10)
    #print(b)
    #print(13+'14')
    d={1:1,2:2,3:3,4:4,}
    #print(d[5])
    l=[1,2,3]
    #print(1[10])
except (ValueError,ZeroDivisionError,NameError,TypeError,KeyError,IndexError):
    print("Error Occured:",e)
else:
    print("No Error Occured")
finally:
    print("ThankYou")'''


'''
try:
    #a=int(input("Enter the age: "))
    #print(12/10)
    print(b)
    #print(13+'14')
    d={1:1,2:2,3:3,4:4,}
    #print(d[5])
    l=[1,2,3]
    #print(1[10])
except Exception as e:
     print("Error Occured:",e)
else:
    print("No Error Occured")
finally:
    print("ThankYou")
'''


'''
try:
    amount=int(input("Enter amount to withdraw:"))
    if amount<0:
        raise Exception("Enter the amount greater than zero:")
except Exception as e:
     print("Error Occured:",e)
else:
    print("No Error Occured")
finally:
    print("ThankYou")            
'''

