Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
d={}
d=dict()
type(d)
<class 'dict'>
d={'k1',:'v1','k2',:'v2'}
SyntaxError: invalid syntax
d={'k1':'v1','k2':'v2'}
d
{'k1': 'v1', 'k2': 'v2'}
d={}
d[1]='int'
d
{1: 'int'}
d[12.3]='float'
d
{1: 'int', 12.3: 'float'}
d['demo']='str'
d
{1: 'int', 12.3: 'float', 'demo': 'str'}
d[2+3j]='complex'
d
{1: 'int', 12.3: 'float', 'demo': 'str', (2+3j): 'complex'}
d[False]='bool'
d
{1: 'int', 12.3: 'float', 'demo': 'str', (2+3j): 'complex', False: 'bool'}
d={}
d[1]=1
d
{1: 1}
d[23]=23.4
d[3]='fghhj'
d[4]=3+4j
d[5]=[1,2,3]
d[6]=(1,2,3)
d[7]={1,3}
d[8]=(1:1,2:2}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
d[8]=(1:1,2:2)
SyntaxError: invalid syntax
d[8]={1:1,2:2}
d[9]=False
d
{1: 1, 23: 23.4, 3: 'fghhj', 4: (3+4j), 5: [1, 2, 3], 6: (1, 2, 3), 7: {1, 3}, 8: {1: 1, 2: 2}, 9: False}
d[1]=14
d
{1: 14, 23: 23.4, 3: 'fghhj', 4: (3+4j), 5: [1, 2, 3], 6: (1, 2, 3), 7: {1, 3}, 8: {1: 1, 2: 2}, 9: False}
d={}
d
{}
d[1]=14
d
{1: 14}
d{}
SyntaxError: invalid syntax
d={}
d[1]=2
d[1]=2 d[1]=2d[1]=2d[1]=2d[1]=2d[1]=2
SyntaxError: invalid decimal literal
d[1]=2
d[2]=2
d[3]=2
d[4]=2
d
{1: 2, 2: 2, 3: 2, 4: 2}
d[3]
2
d={1:2,2:4,3:6,4:8,5:10,6:12}
d[4]
8
d[6]
12
d[1]
2
d[4]
8
d={'harika':89,'subha':67,'maha':56,'gaya':12}
d['harika']
89
d['subha']
67
d['gaya']
12
d.get('harika')
89
d.get('dhanu','user not found')
'user not found'
d.get('harika','user not found')
89
d
{'harika': 89, 'subha': 67, 'maha': 56, 'gaya': 12}
'harika' in d
True
'subha'not in d
False
d.keys()
dict_keys(['harika', 'subha', 'maha', 'gaya'])
d.values()
dict_values([89, 67, 56, 12])
d.items()
dict_items([('harika', 89), ('subha', 67), ('maha', 56), ('gaya', 12)])
sorted(d)
['gaya', 'harika', 'maha', 'subha']
max(d)
'subha'
min(d)
'gaya'
len(d)
4
>>> d
{'harika': 89, 'subha': 67, 'maha': 56, 'gaya': 12}
>>> d['harika']
89
>>> d['harika']=100
>>> d
{'harika': 100, 'subha': 67, 'maha': 56, 'gaya': 12}
>>> d['gaya']=56
>>> d
{'harika': 100, 'subha': 67, 'maha': 56, 'gaya': 56}
>>> d.update({'harika':150,'subha':80})
>>> d
{'harika': 150, 'subha': 80, 'maha': 56, 'gaya': 56}
>>> d.popitem()
('gaya', 56)
>>> d
{'harika': 150, 'subha': 80, 'maha': 56}
>>> d.popitem()
('maha', 56)
>>> d
{'harika': 150, 'subha': 80}
>>> d.pop('subha')
80
>>> d
{'harika': 150}
>>> d.clear()
>>> d
{}
>>> d
{}
>>> d={'harika':89,'subha':67,'maha':56,'gaya':12}
>>> d
{'harika': 89, 'subha': 67, 'maha': 56, 'gaya': 12}
>>> d.set('harika')
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    d.set('harika')
AttributeError: 'dict' object has no attribute 'set'. Did you mean: 'get'?
>>> d.setdefault('harika',0)
89
>>> d
{'harika': 89, 'subha': 67, 'maha': 56, 'gaya': 12}
>>> d.setdefault('dhanu',0)
0
>>> d
{'harika': 89, 'subha': 67, 'maha': 56, 'gaya': 12, 'dhanu': 0}
