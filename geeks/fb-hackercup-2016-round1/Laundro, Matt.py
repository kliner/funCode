import heapq
import Queue

def solve(L, N, M, D, W):
    W.sort()
    pq = []
    for i in xrange(L, 0, -1):
        pq += [-W[0] * i]
    for i in xrange(1, N):
        j = 1
        while -j*W[i] > pq[0]:
            #print -j*W[i] , pq[0]
            heapq.heapreplace(pq, -j*W[i])
            j+=1
        
    q1 = Queue.deque()
    while pq:
        q1.appendleft(-heapq.heappop(pq))
    #print q1

    q2 = Queue.deque()
    for num in q1:
        q2.append(num)
        if len(q2) < M:
            continue
        while num - q2[0] >= D:
            q2.popleft()

    last, ans = 0, 0
    while q2:
        for i in xrange(M):
            if q2:
                t = q2.popleft()
            else:
                return ans + t + D - last
        ans += t + D - last
        last = t

    return ans

f = open('in2.txt')
T = int(f.readline())
for _ in xrange(T):
    L, N, M, D = map(int, f.readline().split())
    W = map(int, f.readline().split())
    print 'Case #%d: %d' % (_+1, solve(L, N, M, D, W))


