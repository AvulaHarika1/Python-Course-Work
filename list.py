Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s='          hello     world      '
s
'          hello     world      '
s.split(_)
['', '']
s.strip()
'hello     world'
s.lstrip()
'hello     world      '
s.rstrip()
'          hello     world'
s='strings.py'
s
'strings.py'
s.startswith('str')
True
s.startwith('ghj')
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    s.startwith('ghj')
AttributeError: 'str' object has no attribute 'startwith'. Did you mean: 'startswith'?
s.startswith('ghj')
False
s.endswith('py')
True
s.endswith('js')
False
'sdffgh'.isalpha()
True
'DFGHJKKLLLLLLLFGH'.isalpha()
True
'harika@12345'.isaplha()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    'harika@12345'.isaplha()
AttributeError: 'str' object has no attribute 'isaplha'. Did you mean: 'isalpha'?
'harika@12345'.isalpha()
False
'ewrtyyui'.islower()
True
'dfgghjjkbhgf#$%T^'.islower()
False
'ASDFGGHHJJ'isupper()
SyntaxError: invalid syntax
'ASDFGGHHJJ'.isupper()
True
' '.isspace()
True
'hello        '.isspace()
False
'py prg lan'.istittle()
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    'py prg lan'.istittle()
AttributeError: 'str' object has no attribute 'istittle'. Did you mean: 'istitle'?
'py prg lan'.istitle()
False
'Py Prg Lan'.istitle()
True
'py_python'.isidentifier()
True
'py@123'.isidentifier()
False
l=[]
l=list()
type(l)
<class 'list'>
l=[1,2,3,4,5]
m=[7,8,9,5,5]
l+m
[1, 2, 3, 4, 5, 7, 8, 9, 5, 5]
l*4
[1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
l=[10,20,30,40,50]
l[4]
50
l[2]
30
l[0]
10
l[-1]
50
l[-3]
30
l[1:4]
[20, 30, 40]
l[::-1]
[50, 40, 30, 20, 10]
l[-1:-4:-1]
[50, 40, 30]
l[-3::-1]
[30, 20, 10]
l
[10, 20, 30, 40, 50]
20 in l
True
10 in l
True
80 in l
False
70 not in l
True
l
[10, 20, 30, 40, 50]
id(l)
2916255277120
l[1]
20
l[1]=70

l
[10, 70, 30, 40, 50]
id(l)
2916255277120
l[4]
50
l
[10, 70, 30, 40, 50]
l[4]=100
l
[10, 70, 30, 40, 100]
l.append(120)
l
[10, 70, 30, 40, 100, 120]
l.append(140)
l
[10, 70, 30, 40, 100, 120, 140]
l.insert(5,50)
l
[10, 70, 30, 40, 100, 50, 120, 140]
l.insert(4,50)
l.extend([80,90,110])
l
[10, 70, 30, 40, 50, 100, 50, 120, 140, 80, 90, 110]
l.pop()
110
l.pop(3)
40
l
[10, 70, 30, 50, 100, 50, 120, 140, 80, 90]
l.pop(1)
70
l
[10, 30, 50, 100, 50, 120, 140, 80, 90]
l.remove(120)
l
[10, 30, 50, 100, 50, 140, 80, 90]
l.remove(90)
l
[10, 30, 50, 100, 50, 140, 80]
>>> del l[1]
>>> l
[10, 50, 100, 50, 140, 80]
>>> del l[3]
>>> l
[10, 50, 100, 140, 80]
>>> l.clear()
>>> l
[]
>>> id(l)
2916255277120
>>> l=[200,300,45,67,51,567,89,909]
>>> sorted(l)
[45, 51, 67, 89, 200, 300, 567, 909]
>>> l.sort()
>>> l
[45, 51, 67, 89, 200, 300, 567, 909]
>>> min(l)
45
>>> max(l)
909
>>> sorted(l,reverse=True)
[909, 567, 300, 200, 89, 67, 51, 45]
>>> l.index(120)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    l.index(120)
ValueError: list.index(x): x not in list
>>> l.index(67)
2
>>> l.count(51)
1
>>> l.count(45)
1
>>> l
[45, 51, 67, 89, 200, 300, 567, 909]
>>> len(l)
8
>>> sum(l)
2228
>>> # 0 0.0 ' ' [] () set() false
>>> any([1,2,3,4,5,5,0,0,0,0,0])
True
>>> all([1,2,3,4,5,5,0,0,0,0,0])
False
