def diff(s1, s2):
    m, n = len(s1), len(s2)
    dp = [ [0] * (n+1) for i in xrange(m+1) ]
    for i in xrange(m):
        for j in xrange(n):
            if s1[i] == s2[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    print dp
    print dp[m][n]
    common = ''
    plus = ''
    minus = ''
    i, j = m, n
    while i > 0 and j > 0:
        if dp[i-1][j] > dp[i][j-1]:
            i -= 1
            minus += s1[i]
        elif dp[i-1][j] < dp[i][j-1]:
            j -= 1
            plus += s2[j]
        else:
            i -= 1
            j -= 1
            common += s1[i]
            
    while i > 0:
        i -= 1
        minus += s1[i]
    while j > 0:
        j -= 1
        plus += s2[j]

    print common[::-1], plus[::-1], minus[::-1]

ori = 'abcddddd'
cur = 'bced'
print diff(ori, cur)

ori = 'bced'
cur = 'abcddddd'
print diff(ori, cur)

#ori = ["first", "second", "fourth"]
#cur = ["first", "fifth"]
#print diff(ori, cur)

        


