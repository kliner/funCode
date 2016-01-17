class Solution(object):

    def editDistance(self, s1, s2):
        m, n = len(s1), len(s2)
        dp = [ [0] * n for i in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                else:
                    if s1[i] == s2[j]:
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1

        return dp[m-1][n-1]

if __name__ == '__main__':
    test = Solution()
    print test.editDistance("sunday", "saturday")

