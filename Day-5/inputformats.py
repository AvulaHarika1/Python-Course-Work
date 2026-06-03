Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
name = input ()
hari
name
'hari'
name = input("enter your name:")
enter your name:harika
name
'harika'
age = input("enter your age:")
enter your age:21
age
'21'
cgp = float(input("enter your cgp:"))
enter your cgp:7.3
cgp
7.3
type(cgp)
<class 'float'>
'harika subha maha sandy gaya'
'harika subha maha sandy gaya'
'harika subha maha sandy gaya'.split(' ')
['harika', 'subha', 'maha', 'sandy', 'gaya']
names = input("enter the names:").split
enter the names:harika sunha mahaa
names
<built-in method split of str object at 0x000002DF086345B0>
names = input("enter the names:").split()
enter the names:subha hari mahaa
names
['subha', 'hari', 'mahaa']
products = input("enter yopur produts:").split()
enter yopur produts:laptop mouse keyboard
products
['laptop', 'mouse', 'keyboard']
topics = tuple(input("enter  your topics:").split())
enter  your topics:token statement
topics
('token', 'statement')
op = set(input ("enter your oper:").split())
enter your oper:in not in is is not and or not
op
{'and', 'is', 'in', 'or', 'not'}
list(map(int,input("enter your marks:").split()))
enter your marks:1 3 4 56
[1, 3, 4, 56]
prices = tuple(map(int,input("enter your prices:").split()))
enter your prices:456 789 234
prices
(456, 789, 234)
rating = set(map(int,input("enter your readings:").split()))
enter your readings:3 4 5 6
rating
{3, 4, 5, 6}
percentage = list(map(float,input("enter your perrcentage:").split()))
enter your perrcentage:56.6 57.8 53.5
percentage
[56.6, 57.8, 53.5]
prices = tuple(map(float,input("enter your prices:").split()))
enter your prices:567 789 123 456
prices
(567.0, 789.0, 123.0, 456.0)
prices = set(map(float,input("enter your prices:").split()))
enter your prices:4565 67878 567 123
prices
{123.0, 4565.0, 67878.0, 567.0}
a,b = 10,20
a
10
b
20
a,b = (10,20)
a
10
b
20
a,b =[10,20]
a
10
b
20
username,password = input("enter the username&password:").split()
enter the username&password:harika har@123
username
'harika'
password
'har@123'
a,b,c,d = list(map,(int,input("enter the 4 sides:").split()))
enter the 4 sides: 4 5 6 7
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    a,b,c,d = list(map,(int,input("enter the 4 sides:").split()))
TypeError: list expected at most 1 argument, got 2
a,b,c,d = list(map(int,input("enter the 4 sides:").split()))
enter the 4 sides:4 5 6 7
a
4
b
5
c
6
d
7
prices,discount = list(map(float,input("enter the prices
                                       
SyntaxError: unterminated string literal (detected at line 1)
prices,discount = list(map(float,input("enter the prices&discounts:").split()))
                                       
enter the prices&discounts:3456 67.8
price
                                       
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    price
NameError: name 'price' is not defined. Did you mean: 'prices'?
prices
                                       
3456.0
discounts
                                       
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    discounts
NameError: name 'discounts' is not defined. Did you mean: 'discount'?
>>> discount
...                                        
67.8
>>> a= eval(input())
...                                        
34456
>>> a
...                                        
34456
>>> a = eval(input())
...                                        
4567.89
>>> a
...                                        
4567.89
>>> a= eval(input())
...                                        
a
>>> (1 2 3 4)
...                                        
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> a
...                                        
4567.89
>>> a= eval(input())
... (1,2,3)
...                                        
SyntaxError: multiple statements found while compiling a single statement
>>> a
...                                        
4567.89
>>> a= eval(input())
...                                        
{3:9,4:16}
>>> a
...                                        
{3: 9, 4: 16}
>>> a
...                                        
{3: 9, 4: 16}
>>> a= eval(input())
... 
...                       
