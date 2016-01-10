floor = 100
x = 1
while x*(x+1)/2 < 100:
    x+=1
    
cur = 0
for i in xrange(x, 0, -1):
    cur = cur + i
    print cur


