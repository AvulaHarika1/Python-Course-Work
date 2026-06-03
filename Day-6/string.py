Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s='python programming'
len(s)
18
sorted(s)
[' ', 'a', 'g', 'g', 'h', 'i', 'm', 'm', 'n', 'n', 'o', 'o', 'p', 'p', 'r', 'r', 't', 'y']
min(s)
' '
max(s)
'y'
ord(s)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    ord(s)
TypeError: ord() expected a character, but string of length 18 found
ord(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    ord(a)
NameError: name 'a' is not defined
ord('a')
97
ord('A')
65
ord('o')
111
ord('')
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    ord('')
TypeError: ord() expected a character, but string of length 0 found
ord(' ')
32
chr(98)
'b'
chr(120)
'x'
chr(30)
'\x1e'
chr(35)
'#'
chr(37)
'%'
s='python programming'
s.upper()
'PYTHON PROGRAMMING'
s.lower()
'python programming'
s.capitalize()
'Python programming'
s.title()
'Python Programming'
s.swapcase()
'PYTHON PROGRAMMING'
s
'python programming'
s.center(28,'-')
'-----python programming-----'
s.ljust(28,'-')
'python programming----------'
s.rjust(28,'-')
'----------python programming'
'123'.zfill(5)
'00123'
'123'.zfill(10)
'0000000123'
'123'.zfill(3)
'123'
'123'.zfill(2)
'123'
s
'python programming'
s.find('g')
10
s.find('o')
4
s.find('z')
-1
s.index('o')
4
s.rindex('o')
9
s.count('y')
1
s.count('m')
2
s.count('g')
2
s
'python programming'
s.replace('python','java')
'java programming'
s.maketrans('python','123445')
{112: 49, 121: 50, 116: 51, 104: 52, 111: 52, 110: 53}
>>> s.translate(s.maketrans('pyton','123445'))
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    s.translate(s.maketrans('pyton','123445'))
ValueError: the first two maketrans arguments must have equal length
>>> s.translate(s.maketrans('python','123445'))
'123445 1r4grammi5g'
>>> s='java,python,javascript,c,c++'
>>> s.split(',')
['java', 'python', 'javascript', 'c', 'c++']
>>> s.split(',',2)
['java', 'python', 'javascript,c,c++']
>>> s.rsplit(',',2)
['java,python,javascript', 'c', 'c++']
>>> g='sdfgh'
>>> g='''dfghghj'''
>>> g='''dfghj
... fghjkl;
... gfjkl
... drtyhj'''
>>> g
'dfghj\nfghjkl;\ngfjkl\ndrtyhj'
>>> s.splitlines()
['java,python,javascript,c,c++']
>>> g.splitlines()
['dfghj', 'fghjkl;', 'gfjkl', 'drtyhj']
>>> l=['java','python','javascript','c','c++']
>>> ''.join(l)
'javapythonjavascriptcc++'
>>> '-'.join(l)
'java-python-javascript-c-c++'
>>> '@'.join(l)
'java@python@javascript@c@c++'
>>> ','.join(l)
'java,python,javascript,c,c++'
>>> s
'java,python,javascript,c,c++'
>>> s.partition(',')
('java', ',', 'python,javascript,c,c++')
>>> s.rpartiotion(',')
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    s.rpartiotion(',')
AttributeError: 'str' object has no attribute 'rpartiotion'. Did you mean: 'rpartition'?
>>> s.rpartition(',')
('java,python,javascript,c', ',', 'c++')
