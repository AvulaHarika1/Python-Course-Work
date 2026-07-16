#syntax
var=lambda agr:exp
add=lambda a,b:a+b


# lambda is shortest form of fun
#exam sum of 2 num
'''add=lambda a,b:a+b
print(add(12,13))
print(add(22,33))'''
#wish
'''
wish=lambda name:f'welcome the python programming course{name}'
print(wish('hari'))
print(wish('dhanu'))'''

#gst
'''
gst=lambda price:price+price*0.18
print(gst(1000))
print(gst(600))
print(gst(89000))'''

#greatest
'''
greatest=lambda a,b:a if a>b else b
print(greatest(18,19))
print(greatest(2000,1900))
print(greatest(10,30))'''

#is even
'''
iseven=lambda a:f"{a}-even number" if a%2==0 else f"{a}-odd number"
print(iseven(4))
print(iseven(9))
print(iseven(25))'''

#charge
'''
bill=lambda charge:charge if charge>99 else charge+30
print(bill(150))
print(bill(45))
print(bill(15))'''


#status
'''
login=True
instock=True
status=lambda login,instock:("you can buy product"if instock
else "product  is out of stock") if login else "login to buy a product"
print(status(login,instock))'''

#list
'''l=[1,2,3,4,5,6,7]
res=list(map(lambda i:i**3,l))
print(res)'''
#nmaes
'''
names=['hari','dhanu','subha','maha']
t=list(map(lambda i:i.title(),names))
print(t)'''

#using filter
#list
'''
l=[1,2,3,4,5,6,7,8,9,10,11,12]
res=list(filter(lambda i:i%2==0,l))
print(res)
'''
'''
l=[1,2,3,4,5,6,7]
res=list(filter(lambda i:i%3==0,l))
print(res)'''

'''l=[1,2,3,4,5,6,7]
res=list(filter(lambda i:i>5,l))
print(res)'''

#reduce
'''
from functools import reduce
l=[1,2,3,4,5,6,7,8,9,10,11,12]
s=reduce(lambda sum,i:sum+i,l)
p=reduce(lambda pro,i:pro*i,l)
print(s,p)'''

#maX ABD MIN
'''
from functools import reduce
l=[1,2,3,4,5,6,7,8,9,10,11,12]
s=reduce(lambda sum,i:sum+i,l)
p=reduce(lambda pro,i:pro*i,l)
m=reduce(lambda max,i: max if max>i else i,l)
mi=reduce(lambda min,i: min if min<i else i,l)
print(s,p,m,mi)'''

#sorted
d={'hari':50,'subha':40,'dhanu':60,'maha':80,'gaya':70}
print(dict(sorted(d.items())))
print(dict(sorted(d.items(),key=lambda i:i[1])))
print(dict(sorted(d.items(),reverse=True)))
print(dict(sorted(d.items(),key=lambda i:i[1],reverse=True)))

