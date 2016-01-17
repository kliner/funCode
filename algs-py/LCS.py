class Solution(object):

    def longestCommonSubsequenceLength(self, s1, s2):
        # length only, dp, time O(mn), mem O(min(n,m))
        m, n = len(s1), len(s2)
        if not m or not n:
            return 0
        if m > n:
            m, n = n, m
            s1, s2 = s2, s1
        lcs = [0] * (n+1)
        for i in xrange(1,m+1):
            for j in xrange(1,n+1):
                if s1[i-1] == s2[j-1]:
                    lcs[i] = lcs[i-1]+1
                else:
                    lcs[i] = max(lcs[i-1], lcs[i])
        return lcs[n]

    def longestCommonSubsequence(self, s1, s2):
        # length only, dp, time O(mn), mem O(mn)
        m, n = len(s1), len(s2)
        if not m or not n:
            return 0
        lcs = [ [0] * (n+1) for i in xrange(m+1)]
        for i in xrange(1,m+1):
            for j in xrange(1,n+1):
                if s1[i-1] == s2[j-1]:
                    lcs[i][j] = lcs[i-1][j-1]+1
                else:
                    lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
        # return lcs[m][n]

        q = []
        i, j = m, n
        while i > 0 and j > 0:
            if s1[i-1] == s2[j-1]:
                q.append(s1[i-1])
                i -= 1
                j -= 1
            else:
                if lcs[i][j] == lcs[i-1][j]:
                    i -= 1
                else:
                    j -= 1

        return ''.join(q[::-1])
    
        
if __name__ == '__main__':
    test = Solution()
    s1 = 'ABCDGH'
    s2 = 'AEDFHR'
    print test.longestCommonSubsequence(s1, s2)
    print test.longestCommonSubsequenceLength(s1, s2)
