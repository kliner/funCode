class MinIndexPQ(object):

    def __init__(self, MAX):
        self.MAX = MAX
        self.N = 0
        self.pq = [(0, 0)] * (MAX+1)
        self.qp = [-1] * (MAX+1)

    def push(self, i, key):
        self.N += 1
        self.pq[self.N] = (key, i)
        self.qp[i] = self.N
        self.swim(self.N)

    def pop(self):
        t, i = self.pq[1]
        self.exch(1,self.N)
        self.N -= 1
        self.sink(1)
        self.qp[i] = -1
        #print self.pq
        return (t, i)

    def containsIndex(self, i):
        return not self.qp[i] == -1

    def decreaseKey(self, i, key):
        k = self.qp[i]
        self.pq[k] = (key, i)
        self.swim(k)

    def swim(self, k):
        while k and self.greater(k>>1,k):
            self.exch(k>>1,k)
            k >>= 1

    def sink(self, k):
        while k*2 <= self.N:
            j = k << 1
            if j < self.N and self.greater(j,j+1):
                j += 1 
            if not self.greater(k, j):
                break
            self.exch(k, j)
            k = j

    def greater(self, i, j):
        return self.pq[i] > self.pq[j]

    def exch(self, i, j):
        t = self.pq[i]
        self.pq[i] = self.pq[j]
        self.pq[j] = t
        self.qp[self.pq[i][1]] = i
        self.qp[self.pq[j][1]] = j

    def size(self):
        return self.N


class Digraph(object):
    def __init__(self, n):
        self.n = n
        self.adj = [[] for i in xrange(n)]

    def addEdge(self, v, w, d):
        self.adj[v].append((w, d))

class Dijkstra(object):
    def __init__(self, G, s):
        n = G.n
        pq = MinIndexPQ(n)
        pq.push(s, 0)
        distTo = [1e10] * n
        distTo[s] = 0
        
        def relax(v, w, d):
            if distTo[w] > distTo[v]+d:
                distTo[w] = distTo[v]+d
                if pq.containsIndex(w):
                    pq.decreaseKey(w, distTo[w])
                else:
                    pq.push(w, distTo[w])

        while pq.size():
            t, v = pq.pop()
            for w, d in G.adj[v]:
                relax(v, w, d)

        self.distTo = distTo

    def get(self, w):
        return self.distTo[w]

T = input()
for _ in xrange(T):
    n = input()
    G = Digraph(n)
    dct = {}
    for v in xrange(n):
        s = raw_input()
        dct[s] = v
        m = input()
        for _a in xrange(m):
            w, d = map(int, raw_input().split())
            w -= 1
            G.addEdge(v, w, d)
    t = input()
    dd = {}
    for _b in xrange(t):
        v, w = map(dct.get, raw_input().split())
        if v not in dd:
            d = Dijkstra(G, v)
            print d.get(w)
            dd[v] = d
        else:
            d = dd[v]
            print d.get(w)
    raw_input()
    
    
