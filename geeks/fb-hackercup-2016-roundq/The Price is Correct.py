import bisect

f = open('input3.txt')
T = int(f.readline())
for _ in xrange(T):
    N, p = f.readline().split()
    N, p = int(N), int(p)
    s = f.readline().split()
    B = [int(s[i]) for i in xrange(N)]
    S = [B[0]] * N
    for i in xrange(1, N):
        S[i] = S[i-1]+B[i]

    def getSum(i, j):
        return S[j] - S[i]

    def merge(lhi, rlo):
        #print lhi, rlo
        ans = 0
        if not lhi or not rlo:
            return 0
        for x in lhi:
            idx = bisect.bisect(rlo, p - x)
            ans += idx
        #print ans
        return ans

    def solve(lo, hi):
        if lo == hi and B[lo] <= p:
            return 1, [B[lo]], [B[hi]]
        elif lo == hi and B[lo] > p:
            return 0, [], []
        m = (lo+hi)>>1
        left_cnt, left_lo, left_hi = solve(lo, m)
        right_cnt, right_lo, right_hi = solve(m+1, hi)
        #print left_lo, left_hi, right_lo, right_hi
        #print lo, hi, m
        center = merge(left_hi, right_lo)
        idx = m+1
        while idx <= hi and left_lo and left_lo[-1]+B[idx] <= p:
            left_lo.append(left_lo[-1]+B[idx])
            idx += 1
        #print left_lo
        idx = m
        while idx >= lo and right_hi and right_hi[-1]+B[idx] <= p:
            right_hi.append(right_hi[-1]+B[idx])
            idx -= 1
        #print right_hi 
        return left_cnt+right_cnt+center, left_lo, right_hi

    #print N, p, B
    print 'Case #%d: %d' % (_+1, solve(0, N-1)[0])
        
