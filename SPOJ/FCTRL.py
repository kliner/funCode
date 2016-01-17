debug = 0

# ------------init--------------
t = 5
dct = [(5,1)]
while t < 1000000000:
    last, cnt = dct[-1]
    t *= 5 
    dct.append((t, cnt*5+1))

# ----------solution------------
def solve(n):
    ans = 0
    for k, cnt in dct[::-1]:
        if n >= k:
            ans += (n / k)*cnt
            n = n % k
    print ans

# ------------test--------------
if debug:
    solve(3)
    solve(25)
    solve(60)
    solve(100)
    solve(1024)
    solve(23456)
    solve(8735373)

# ------------main--------------
T = input()
for _ in xrange(T):
    solve(input())
