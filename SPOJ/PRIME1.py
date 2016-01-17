import math

def solve(m, n, dct):
    maxn = int(math.sqrt(n))
    for i in xrange(m, n+1):
        for x in dct:
            if i == x or x > maxn:
                print i
                break
            if i % x == 0:
                break
        else:
            print i

T = input()
dct = []
N = 100000
a = [1] * N
for i in xrange(2, N):
    if a[i]:
        dct += [i]
        j = i
        while j < N:
            a[j] = 0
            j += i
#print dct[:100]
#print len(dct)

for _ in xrange(T):
    x, y = map(int, raw_input().split())
    if y == 1:
        print
        continue
        
    if x == 1:
        x += 1
    solve(x, y, dct)
    print 
    
