f = open('text_editor.in')
T = int(f.readline())
for _ in xrange(T):
    N, K = f.readline().split()
    N, K = int(N), int(K)
    strs = [f.readline().strip() for i in xrange(N)]
    strs.sort()
    dst = [[0] * N for i in xrange(N)]

    def dist(s1, s2):
        #print s1, s2
        l1, l2 = len(s1),len(s2)
        n = min(l1, l2)
        for i in xrange(n):
            if s1[i] != s2[i]:
                return l1+l2-i*2+1
        return l1+l2-n*2+1

    dp = [[1e10] * (K+1) for i in xrange(N)]
    for i in xrange(N):
        dp[i][0] = len(strs[i])+1

    for i in xrange(N):
        for j in xrange(i+1, N):
            dst[i][j] = dist(strs[i], strs[j])
            dst[j][i] = dst[i][j]
    #print dst

    # do[i][0] = len(s[i])
    # dp[i][j] indicated for min using j cnt num, ending in i 
    # dp[i][j] = min( dp[k][j-1]+dist[k][i] )
    def solve():
        for i in xrange(N):
            for j in xrange(K-1):
                for k in xrange(i):
                    dp[i][j+1] = min(dp[i][j+1], dp[k][j] + dst[k][i])
        #print dp
        ans = 1e10
        for i in xrange(N):
            ans = min(ans, dp[i][K-1] + len(strs[i]))
        return ans

    print 'Case #%d: %d' % (_+1, solve())
