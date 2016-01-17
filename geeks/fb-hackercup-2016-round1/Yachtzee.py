'''
a = [8,2]
ans = 1.5
for n in a:
    ans+=n**2/2
print ans / (20-9)


a = [4,9,1,12,7]
ans = 0.0
for n in a:
    ans+=n**2/2.0
print ans 
a1 = ans

a = [1,12,7]
ans = (3+9)*6/2.
for n in a:
    ans+=n**2/2.0
print ans 
a2 = ans

a = [4,4]
ans = 0.0
for n in a:
    ans+=n**2/2.0
print ans 

print a1*2+a2+ans
'''

import bisect 
import math

def solve(N, A, B, C):
    S = [0]
    total = 0
    for n in C:
        S += [S[-1]+n]
        total += n*n/2.
    #print total

    a = A % S[-1]
    lo = bisect.bisect(S, a)
    a -= S[lo-1]
    start = (a+C[lo-1])*(C[lo-1]-a)/2.
    for i in xrange(lo, N):
        start += C[i]*C[i]/2.
    #print start
    
    b = B % S[-1]
    hi = bisect.bisect(S, b)
    b -= S[hi-1]
    end = b*b/2.
    for i in xrange(hi-1):
        end += C[i]*C[i]/2.
    #print end

    #print (B/S[-1]-math.ceil(float(A)/S[-1]))
    return (start+end+(B/S[-1]-math.ceil(float(A)/S[-1]))*total)/(B-A)

f = open('in3.txt')
T = int(f.readline())
for _ in xrange(T):
    N, A, B = map(int, f.readline().split())
    C = map(int, f.readline().split())
    print 'Case #%d: %.8f' % (_+1, solve(N, A, B, C))

