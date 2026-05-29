Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
type(a)
<class 'int'>
t=51.45
type(t)
<class 'float'>
c=12+5j
type(c)
<class 'complex'>
s="harika"
type(s)
<class 'str'>
s='''harika'''
type(s)
<class 'str'>
l=[1,2,3]
>>> id(l)
1519994666560
>>> l=['post1.png','reel1.mp4']
>>> l
['post1.png', 'reel1.mp4']
>>> l=[]
>>> l=list()
>>> type(l)
<class 'list'>
>>> t=(1,2,3,4)
>>> t
(1, 2, 3, 4)
>>> type(t)
<class 'tuple'>
>>> s=(1,2,3,4,6)
>>> type(s)
<class 'tuple'>
>>> s=set()
>>> s=(456,678,178,12234)
>>> a
10
>>> s
(456, 678, 178, 12234)
>>> d={'name':'age':100,'course':'psf')
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
>>> d=={'name':'age':100,'course':'psf'}
SyntaxError: invalid syntax
>>> d={'name':'abc','age':100,'course':'psf'}
>>> d
{'name': 'abc', 'age': 100, 'course': 'psf'}
>>> type(d)
<class 'dict'>
>>> status=true
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    status=true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> status=True
>>> status=False
>>> type(status)
<class 'bool'>
>>> type(a)
<class 'int'>
>>> a=None
>>> type(a)
<class 'NoneType'>
