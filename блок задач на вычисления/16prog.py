p = int(input())
x = int(input())
y = int(input())
from math import floor
print((100*x+y+p/100*(100*x+y))//100, floor((100*x+y+p/100*(100*x+y))%100))
