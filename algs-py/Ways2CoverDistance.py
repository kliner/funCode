def Ways2CoverDistance(n):
    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    for i in xrange(3, n+1):
        dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
    return dp[n]

print Ways2CoverDistance(4)
