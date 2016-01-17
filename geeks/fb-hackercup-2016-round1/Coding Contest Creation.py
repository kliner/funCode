
def solve(N, a):
    #print a
    ans = 0
    q = []
    i = 0
    while i < N:
        n = a[i]
        if len(q) == 4:
            q = [n]
            i += 1
        elif not q or 0<n-q[-1]<=10:
            q += [n]
            i += 1
        elif n <= q[-1]:
            ans += 4-len(q)
            q = [n]
            i += 1
        else:
            q += [q[-1]+10]
            ans += 1
        #print q

    ans += 4-len(q)
    return ans

f = open('in1.txt')
T = int(f.readline())
for _ in xrange(T):
    N = int(f.readline())
    a = map(int, f.readline().split())
    print 'Case #%d: %d' % (_+1, solve(N, a))

