import sys 

# Als je je python script runned door:
#  'python sysspec.py --1 --2' te runnen, 
# geef je argumenten mee aan je bestand die je met sys.argv kan opvragen
print(list(sys.argv)[2])


import os 

print(os.listdir())

import datetime as d

now = d.datetime.now()
x = now.strftime('%Y-%m-%d')
print(x)
now_new = d.datetime.strptime(x, '%y-%m-%d')
print(now_new)