def dst(p1, p2):
    return (p1[0]-p2[0])*(p1[0]-p2[0])+(p1[1]-p2[1])*(p1[1]-p2[1])

def solve(points):
    n = len(points)
    #dist = [[0] * n for _ in xrange(n)]
    dct = {}
    for i in xrange(n):
        for j in xrange(i+1, n):
            #dist[i][j] = dst(points[i], points[j])
            a = dst(points[i], points[j])
            if a in dct:
                dct[a] += [(i,j)]
            else:
                dct[a] = [(i,j)]
    #print dist
    #print dct
    ans = 0
    for i in dct.keys():
        #dct[i].sort()
        dct2 = {}
        for j in xrange(len(dct[i])):
            p = dct[i][j]
            if p[0] in dct2:
                dct2[p[0]] += 1
            else:
                dct2[p[0]] = 1
            if p[1] in dct2:
                dct2[p[1]] += 1
            else:
                dct2[p[1]] = 1

        for v in dct2.values():
            ans += (v*(v-1)/2)
    return ans


f = open('input1.txt')
T = int(f.readline())
for _ in xrange(T):
    N = int(f.readline())
    points = []
    for i in xrange(N):
        t = f.readline().split()
        points += [(int(t[0]), int(t[1]))]
    print 'Case #%d: %d' % (_+1, solve(points))
