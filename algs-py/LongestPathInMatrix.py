di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def find(i, j, n, mat, dp):
    if dp[i][j] != None:
        return dp[i][j]
    for t in xrange(4):
        x = i + di[t]
        y = j + dj[t]
        if x >= 0 and x < n and y >= 0 and y < n and mat[x][y] == mat[i][j] - 1:
            dp[i][j] = find(x, y, n, mat, dp) + 1
            return dp[i][j]
    dp[i][j] = 1
    return 1


def LongestPathInMatrix(mat):
    n = len(mat)
    if n == 0:
        return 0
    dp = [ [None] * n for _ in xrange(n) ]
    ans = 0
    for i in xrange(n):
        for j in xrange(n):
            ans = max(ans, find(i,j,n,mat,dp))
    print dp
    return ans
            
mat = [ [1,2,3],
        [5,9,8],
        [4,6,7] ]
print LongestPathInMatrix(mat)
