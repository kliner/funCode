class Guard(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ax = True
        self.ay = True

def update(i, l, N):
    for j in xrange(i+1, N):
        if l[j] == '.':
            l[j] = 'X'
        else:
            return j

def update2(i, l1, l2, N):
    a1, a2 = None, None
    for a1 in xrange(i+1, N):
        if l1[a1] != '.':
            break
    for a2 in xrange(i+1, N):
        if l2[a2] != '.':
            break
    if not a1 and not a2:
        return 0
    elif a1 < a2:
        update(i, l1, N)
    else:
        update(i, l2, N)
    return a1 < a2

def solve(N, l1, l2):
    ans = 0
    lastGuard = None
    for i in xrange(N):
        if l1[i] == 'X' and l2[i] == 'X':
            if lastGuard:
                lastGuard = None
                ans += 1
        elif l1[i] == '.' and l2[i] == '.':
            if not lastGuard:
                lastGuard = Guard(i, 1)
                lastGuard.ax = False
            elif lastGuard.ax:
                if lastGuard.y == 1:
                    update(i, l1, N)
                else:
                    update(i, l2, N)
                lastGuard = None
                ans += 1
            else:
                if update2(i, l1, l2, N):
                    lastGuard = Guard(i, 2)
                    lastGuard.ay = False
                else:
                    lastGuard = Guard(i, 1)
                    lastGuard.ay = False
                ans += 1

        elif l1[i] == '.' and l2[i] == 'X':
            if not lastGuard:
                lastGuard = Guard(i, 1)
                lastGuard.ay = False
            elif lastGuard.ay:
                lastGuard = None
                update(i, l1, N)
                ans += 1
            elif lastGuard.y != 1:
                lastGuard = None
                ans += 1
        elif l1[i] == 'X' and l2[i] == '.':
            if not lastGuard:
                lastGuard = Guard(i, 2)
                lastGuard.ay = False
            elif lastGuard.ay:
                lastGuard = None
                ans += 1
                update(i, l2, N)
            elif lastGuard.y != 2:
                lastGuard = None
                ans += 1
    if lastGuard:
        ans += 1
    return ans
        

f = open('input2.txt')
T = int(f.readline())
for _ in xrange(T):
    N = int(f.readline())
    l1 = f.readline()
    l2 = f.readline()
    a1 = [ch for ch in l1]
    a2 = [ch for ch in l2]
    print 'Case #%d: %d' % (_+1, solve(N, a1, a2))

