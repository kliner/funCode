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
        
    print N
    q1 = Queue.deque()
    while pq:
        q1.appendleft(-heapq.heappop(pq))
    #print q1

    if M >= L:
        return q1[-1]+D

    q2 = Queue.deque()
    for i in xrange(M):
        q2.appendleft(q1.popleft()+D)

    for i in xrange(M, L):
        t = max(q2.pop(), q1.popleft())
        q2.appendleft(t+D)
        
    ans = q2.popleft()
    return ans

f = open('./round1/laundro_matt.in')
T = int(f.readline())
for _ in xrange(T):
    L, N, M, D = map(int, f.readline().split())
    W = map(int, f.readline().split())
    print 'Case #%d: %d' % (_+1, solve(L, N, M, D, W))


