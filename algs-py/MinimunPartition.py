def MinimumPartiion(nums):
    total = sum(nums)
    n = len(nums)
    if n == 0:
        return total
    dp = [ [0] * total for i in xrange(n+1) ]
    for i in xrange(n):
        dp[i][0] = 1

    for i in xrange(n):
        for j in xrange(nums[i], total):
            dp[i+1][j] = dp[i][j]
            if dp[i][j-nums[i]]:
                dp[i+1][j] = dp[i][j-nums[i]]

    print dp
    for i in xrange(total>>1, -1, -1):
        if dp[n][i]:
            return total-i*2

def MinimumPartiionSpaceM(nums):
    total = sum(nums)
    n = len(nums)
    if n == 0:
        return total
    dp = [0] * total
    dp[0] = 1

    for i in xrange(n):
        for j in xrange(total-1, nums[i]-1, -1):
            dp[j] |= dp[j-nums[i]]

    print dp
    for i in xrange(total>>1, -1, -1):
        if dp[i]:
            return total-i*2

arr = [3,1,4,2,2,1]
print MinimumPartiion(arr)
print MinimumPartiionSpaceM(arr)
arr = [3,4,2,1]
print MinimumPartiion(arr)
print MinimumPartiionSpaceM(arr)
arr = [3,4,4]
print MinimumPartiion(arr)
print MinimumPartiionSpaceM(arr)
