debug = 1

# ------------init--------------

# ----------solution------------
# cannot pass the SPOJ. plz using C/C++/Java
def solve(s):
    n = len(s)
    t = s[::-1]
    dp = [0] * (n+1)
    last = [0] * (n+1)
    for i in xrange(1, n+1):
        for j in xrange(1, n+1):
            if s[i-1]==t[j-1]:
                dp[j] = last[j-1]+1
            else:
                dp[j] = max(dp[j-1], last[j])
        last, dp = dp, last
    print n-last[n]


# ------------test--------------
if debug:
    solve("fft")
    solve("abcba")
    solve("abccba")
    solve("abcabc")
    solve("abca")
    solve("abaa")
    solve("aaba")

# ------------main--------------
T = input()
for _ in xrange(T):
    solve(raw_input())

