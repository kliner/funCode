def knapSack(W, wt, val):
    n = len(wt)
    dp = [0] * (W+1)
    for i in xrange(n):
        for j in xrange(W, wt[i]-1, -1):
            dp[j] = max(dp[j], dp[j-wt[i]]+val[i])
    print dp
    return dp[W]

val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
print knapSack(W, wt, val)
