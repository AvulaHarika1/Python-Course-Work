#recursive:
''' def func()
          if  base
return
fun()
'''

#recursive
'''
def func(num):
    if num==0:
        return
    print(num,end=' ')
    func(num-1)
    print(num,end=' ')
func(5)
    '''
#sum of N natural numbers
'''
def  sumofdigits(n):
    if n==0:
        return 0
    return n+sumofdigits(n-1)
print(sumofdigits(5))
    '''
#product of num
'''
def  productofdigits(n):
    if n==0:
        return 1
    return n*productofdigits(n-1)
print(productofdigits(5))'''

#power cal
'''
def power(base,pow):
    if pow==0:
        return 1
    return base*power(base,pow-1)
print(power(2,4))
print(power(5,2))'''

#reverse a string
'''def reverseofstr(s,ind):
    if ind == 0:
        return s[0]
    return s[ind]+reverseofstr(s,ind-1)
l="Python Programming"
print(reverseofstr(l,len(l)-1))'''


#print string pattern
'''def display(s,ind):
    if ind==len(s):
        return
    print(s[:ind+1])
    display(s,ind+1)
display("python",0)'''
#abcdef,3 -> abc,bcd,cde,def
#abcdef,4 ->abcd,bcde,cdef

'''def display(s,ind):
    if ind==len(s):
        return
    print(s[:ind+1])
    display(s,ind+1)
display("python",0)'''

#sum of dig
'''def display(l,ind):
    if ind == len(l):
        return 0
    return l[ind]+display(l,ind+1)
l=[1,2,4,5,7,3,5,6]
print(display(l,0))'''

#count of vowels in a str
'''
def display(s,i):
    if i==len(s):
        return 0
    if s[i] in 'aeiouAEIOU':
        return 1+display(s,i+1)
    else:
        return display(s,i+1)
s='python programming'
print(display(s,0))'''


