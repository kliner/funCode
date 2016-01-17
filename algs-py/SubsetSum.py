def isSubsetSum(nums, query):
    n = len(nums)
    if n == 0:
        return False
    total = sum(nums)
    if query > total:
        return False
    if query == total or query == 0:
        return True
    dp = [0] * total
    dp[0] = 1
    for i in xrange(n):
        for j in xrange(total-1, nums[i]-1, -1):
            dp[j] |= dp[j-nums[i]]
    print dp
    return dp[query] == 1

print isSubsetSum([3, 34, 4, 12, 5, 2], 9)
print isSubsetSum([3, 34, 4, 12, 5, 2], 1)
print isSubsetSum([3, 34, 4, 12, 5, 2], 13)
print isSubsetSum([3, 34, 4, 12, 5, 2], 33)
