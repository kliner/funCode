import Queue
import copy

def solve(N, M):
    if N == 1:
        return [[1, 1]]
    ans = [[0,(N>>1)+1] for i in xrange(N)]
    for i in xrange(N):
        if sum(M[i]) == N-1:
            ans[i][1] = 1

    marked = [0] * N 

    rank = {16: [9,5,3,2,1], 8:[5,3,2,1], 4:[3,2,1], 2:[2,1]}
    
    def parse(arr):
        #print arr
        t = copy.copy(arr)
        for i in xrange(N >> 1):
            for j in xrange(N >> (1+i)):
                if M[t[2*j]][t[2*j+1]]:
                    t[j] = t[2*j]
                    ans[t[2*j]][0] = max(ans[t[2*j]][0], i+1)
                else:
                    t[j] = t[2*j+1]
                    ans[t[2*j+1]][0] = max(ans[t[2*j+1]][0], i+1)


    def dfs(arr):
        if len(arr) == N:
            parse(arr)
            return
        
        for i in xrange(N):
            if not marked[i]:
                marked[i] = 1
                arr.append(i)
                break

        for j in xrange(i, N):
            if not marked[j]:
                marked[j] = 1
                arr.append(j)
                dfs(arr)
                arr.pop()
                marked[j] = 0

        arr.pop()
        marked[i] = 0
    
    dfs(Queue.deque())
    
    for i in xrange(N):
        #print ans[i][0]
        ans[i][0] = rank[N][ans[i][0]]
    return ans

f = open('in4.txt')
T = int(f.readline())
for _ in xrange(T):
    N = int(f.readline())
    M = []
    for i in xrange(N):
        M.append(map(int, f.readline().split()))
    print 'Case #%d:' % (_+1)
    a = solve(N, M)
    for i in xrange(N):
        print a[i][0],a[i][1]

