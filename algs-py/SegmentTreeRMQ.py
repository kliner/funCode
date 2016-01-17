import math
class SegmentTreeRMQ(object):

    def __init__(self, arr):
        self.n = len(arr)
        height = int(math.ceil(math.log(len(arr), 2)))
        self.st = [None for i in xrange(2 ** (height+1) - 1)]
        print len(self.st)
        self.build(arr, 0, len(arr)-1, 0)
        print self.st

    def build(self, arr, lo, hi, idx):
        if lo == hi:
            self.st[idx] = arr[lo]
            return arr[lo]
        m = (lo+hi) >> 1
        self.st[idx] = min(self.build(arr, lo, m, idx*2+1), self.build(arr, m+1, hi, idx*2+2))
        return self.st[idx]

    def RMQ(self, lo, hi):
        return self.query(0, self.n-1, lo, hi, 0)

    def query(self, slo, shi, qlo, qhi, idx):
        if qlo <= slo and shi <= qhi:
            # complete in query range
            return self.st[idx]
        if qlo > shi or qhi < slo:
            # comlete not in query range
            return 1e10
        # intersect, binary search
        m = (slo+shi) >> 1
        return min(self.query(slo, m, qlo, qhi, idx*2+1), self.query(m+1, shi, qlo, qhi, idx*2+2))

    def update_st(self, lo, hi, cur, idx, value): 
        if lo == hi:
            self.st[cur] = value
            return self.st[cur]
        m = (lo+hi)>>1
        if idx <= m:
            self.st[cur] = min(self.st[cur*2+2], self.update_st(lo, m, cur*2+1, idx, value))
        elif idx > m:
            self.st[cur] = min(self.st[cur*2+1], self.update_st(m+1, hi, cur*2+2, idx, value))
        return self.st[cur]

    def update(self, idx, value):
        self.update_st(0, self.n-1, 0, idx, value)
        print self.st
        

if __name__ == '__main__':
    a = [1, 3, 2, 7, 9, 11]
    test = SegmentTreeRMQ(a)
    print test.RMQ(1,5)
    test.update(2,4)
    print test.RMQ(1,5)
    test.update(1,2)
    print test.RMQ(1,5)
    test.update(5,1)
    print test.RMQ(1,5)

