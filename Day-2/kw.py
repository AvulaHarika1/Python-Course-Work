Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> Myvar=10
>>> Myvar1=10
>>> Myvar@1=10
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
>>> my_var=10
>>> my var=10
SyntaxError: invalid syntax
>>> myvar=10
>>> Myvar=10
>>> myvar
10
>>> Myvar
10
>>> var=10
>>> var=20
>>> var
20
>>> var
20
>>> a=10
>>> b=20
>>> a
10
>>> b
20
>>> a=b=c=10
>>> a
10
>>> b
10
>>> c
10
>>> a,b,c=30
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a,b,c=30
TypeError: cannot unpack non-iterable int object
>>> a
10
>>> a,b,c=10,20,30
>>> a
10
>>> b
20
>>> c
30
a,b=7,5
a,b=b,a
a
5
b
7
