debug = 0

def notless(s1, s2):
    n = len(s1)
    for i in xrange(n):
        if s1[i] < s2[i]:
            return 1
        elif s2[i] < s1[i]:
            return 0
    else:
        return 1

if debug:
    print notless('21', '33')
    print notless('21', '21')
    print notless('44', '33')

def inc(s):
    n = len(s)
    ret = ''
    for i in xrange(n-1, -1, -1):
        if s[i] == '9':
            ret += '0'
        else:
            ret += chr(ord(s[i])+1)
            return s[:i]+ret[::-1], 0
    return '1'+ret, 1

if debug:
    print inc('100')
    print inc('999')
    print inc('19')

def solve(s):
    l = len(s)
    m = l >> 1
    even = l % 2
    if even:
        left = s[:m+1]
    else:
        left = s[:m]
    right = s[m:]
    ori = left
    left = left[::-1]
    if notless(left, right):
        t, f = inc(ori) 
        if even:
            if f:
                print t[:-1]+t[-2::-1]
            else:
                print t+t[-2::-1]
        else:
            if f:
                print t+t[-2::-1]
            else:
                print t+t[::-1]
    else:
        t = ori
        if even:
            print t+t[-2::-1]
        else:
            print t+t[::-1]

if debug:
    solve('808')
    solve('898')
    solve('899')
    solve('2133')
    solve('233')
    solve('1')
    solve('9')
    solve('99')
    solve('999')
    solve('989')
    solve('998')
    solve('1000')
    solve('9999999999999999')
T = input()
for _ in xrange(T):
    solve(raw_input())
