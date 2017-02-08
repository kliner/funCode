debug = 0

# ------------init--------------

# ----------solution------------
def solve(s):
    dp = [0] * (len(s)+1)
    dp[0] = 1
    dp[1] = 1
    for i in xrange(1, len(s)):
        if s[i] == '0':
            dp[i+1] = dp[i-1]
        elif s[i-1] == '1' or (s[i-1] == '2' and s[i] in ('1', '2', '3', '4', '5', '6')):
            dp[i+1] = dp[i] + dp[i-1]
        else:
            dp[i+1] = dp[i]
    return dp[len(s)]


# ------------test--------------
if debug:
    print solve('25114')
    print solve('25104')
    print solve('27104')

# ------------main--------------
s = raw_input()
while s != '0':
    print solve(s)
    s = raw_input()

