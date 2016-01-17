def optimalStrategyOfGame(nums):
    n = len(nums)
    if n == 0:
        return 0
    if n < 2:
        return max(nums)
    dp = [ [0] * n for t in xrange(n)]
    for i in xrange(n):
        dp[i][i] = nums[i]
    for i in xrange(n-1):
        dp[i][i+1] = max(nums[i], nums[i+1])
    print dp
    for i in xrange(2, n):
        for j in xrange(i, n):
            dp[j-i][j] = max( min(dp[j-i+2][j], dp[j-i+1][j-1]) + nums[j-i], min(dp[j-i][j-2], dp[j-i+1][j-1]) + nums[j] )
    print dp
    return dp[0][n-1]
    
nums = [8, 15, 3, 7]
print optimalStrategyOfGame(nums)
nums = [2, 2, 2, 2]
print optimalStrategyOfGame(nums)
nums = [20, 30, 2, 2, 2, 10]
print optimalStrategyOfGame(nums)
