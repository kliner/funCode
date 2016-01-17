class Digraph(object):
    def __init__(self, n):
        self.n = n
        self.adj = [[] for i in xrange(n)]

    def addEdge(self, v, w, d):
        self.adj[v].append((w, d))

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

t = MinIndexPQ(100)
t.push(1, 100)
t.push(2, 20)
t.push(3, 10)
t.push(4, 80)
print t.containsIndex(1)
print t.pop()
print t.pop()
print t.containsIndex(3)
t.push(3, 33)
print t.containsIndex(3)
t.decreaseKey(4, 20)
print t.pop()
print t.pop()
print t.pop()

class Dijkstra(object):
    def __init__(self, G, s):
        n = G.n
        pq = MinIndexPQ(n)
        distTo = [1e10] * n
        distTo[s] = 0
        edgeTo = [None] * n
        pq.push(s, 0)
        
        def relax(v, w, d):
            if distTo[w] > distTo[v]+d:
                distTo[w] = distTo[v]+d
                edgeTo[w] = v
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

G = Digraph(4)
G.addEdge(0,1,1)
G.addEdge(0,2,3)
G.addEdge(1,0,1)
G.addEdge(1,2,1)
G.addEdge(1,3,4)
G.addEdge(2,0,3)
G.addEdge(2,1,1)
G.addEdge(2,3,1)
G.addEdge(3,1,4)
G.addEdge(3,2,1)
d = Dijkstra(G, 0)
print d.distTo
d = Dijkstra(G, 1)
print d.distTo
d = Dijkstra(G, 2)
print d.distTo
d = Dijkstra(G, 3)
print d.distTo
