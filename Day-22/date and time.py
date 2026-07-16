#date and time module
'''
from datetime import date,time,datetime,time
t=date.today()
print(t)
print("year:",t.year)
print("month:",t.month)
print("day:",t.day)
print("weekday from 0:",t.weekday())
print("weekday from 0:",t.isoweekday())
'''

#creating aspecific date
'''
from datetime import date,time,datetime,time
t=date(2026,11,30)
print(t)
'''
#extracting hrs,min,sec
'''
from datetime import date,time,datetime,time
t=time(23,59,0)
print(t)
'''
#getting the current date and time
'''
from datetime import date,time,datetime,time
n=datetime.now()
print(n)
print("year:",n.year)
print("month:",n.month)
print("day:",n.day)
print("hour:",n.hour)
print("minute:",n.minute)
print("second:",n.second)
'''
#

from datetime import date,time,datetime,time

'''
n=datetime.now()
print(n.strftime('%d/%m/%y'))
print(n.strftime('%d/%m/%y %H:%M:%S'))
print(n.strftime('%d/%m/%y %I:%M:%S:%P'))
print(n.strftime('%d %b %y %I:%M:%S:%P'))
print(n.strftime('%d %B %y% I:%M:%S:%P'))
print(n.strftime('%a,%d %B,%Y %I:%M:%S:%P'))
print(n.strftime('%A, %d %B,%Y %I:%M:%S:%P'))'''

#

from datetime import date,time,datetime,timedelta
n=datetime.now()
n15=n+timedelta(minutes=15)
n2=n+timedelta(hours=2)
n7=n+timedelta(days=60)
print(n15,n2,n7,sep='\n')

