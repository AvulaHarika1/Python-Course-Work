Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=20
b=10
a+b
30
a-b
10
a*b
200
a/b
2.0
9/2
4.5
9//2
4
a**b
10240000000000
a**2
400
6**3
216
a%b
0
17%4
1
17%3
2
a=20
b=10
a<b
False
a>b
True
a<=b
False
a>=b
True
a==b
False
a!=b
True
y=5
y
5
y=y+5
y
10
y=y+10
y
20
y+=1=
SyntaxError: invalid syntax
y+=10
y
30
y-=10
y%=2
y
0
y+=10
y
10
y/=2
y
5.0
y//=2
y
2.0
logiccal chepthunaru
SyntaxError: invalid syntax
a
20
b
10
a%10==0
True
a%20==0 and b%20==0 and a>b
False
a%20==0 or b%20==0 or a>b
True
a%20==0 or b%20==0 or a<b
True
a%22==0 or b%22==0 or a<b
False
not a>b
False
not a<b
True
membership chepthunaru
SyntaxError: invalid syntax
#str,list,dict,set,tuple
a='harika'
'a' in a
True
'b' in a
False
'b' not in a
True
l=['java','python','mysql','c++','c','html']
'mysql' in l
True
'c' not in l
False
t=('laptop','mobile','mouse','keyboard')
t
('laptop', 'mobile', 'mouse', 'keyboard')
'laptop' in  t
True
'mouse' in t
True
'charger' in t
False
t={1,2,3,4,5,567,789}
50 not in t
True
1 in t
True
d={'egg':8,'oil':120,'sugar':40,'salt':27}
'oil' in d
True
28 in d
False
'sugar' in d
True
identity chep
SyntaxError: invalid syntax
l={1,2,3,4,5}
m={1,2,3,4,5}
l==m
True
n
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    n
NameError: name 'n' is not defined
n=m
n
{1, 2, 3, 4, 5}
l is m
False
n is m
True
id(l)
1936898728320
id(n)
1936897766144
id(m)_
SyntaxError: invalid syntax
id(m)
1936897766144
l is not m
True
m in n
False
n is not l
True
bitwise chepthunaru
SyntaxError: invalid syntax
8 $ 14
SyntaxError: invalid syntax
8 & 14
8
8 & 7
0
8 | 7
15
>>> 10^11
1
>>> 1
1
>>> ~12
-13
>>> 8>>2
2
>>> 15>>3
1
>>> 15>>2
3
>>> 16<<1
32
>>> 16<<2
64
>>> 4<<2
16
>>> a=12
>>> b=12.34
>>> c='python'
>>> print(a,b,c)
12 12.34 python
>>> print("a=",a,'b=',b,'c=',c,sep='',end='@@@@')
a=12b=12.34c=python@@@@
>>> print(f'a= {a} b= {b} c= {c}'}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
>>> print(f'a= {a} b= {b} c= {c}')
a= 12 b= 12.34 c= python
>>> print('a= %d b.2f c%s'%(a,b,c))
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    print('a= %d b.2f c%s'%(a,b,c))
TypeError: not all arguments converted during string formatting
>>> print('a= %d b.2f c=%s'%(a,b,c))
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    print('a= %d b.2f c=%s'%(a,b,c))
TypeError: not all arguments converted during string formatting
>>> print('a= %d b=%.2f c=%s'%(a,b,c))
a= 12 b=12.34 c=python
>>> print('a={} b={} c=%s'%(a,b,c))
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    print('a={} b={} c=%s'%(a,b,c))
TypeError: not all arguments converted during string formatting
