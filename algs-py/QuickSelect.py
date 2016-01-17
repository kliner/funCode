import random
'''
find the kth smallest element
on average O(n)
'''
def exch(a, i, j):
    t = a[i] 
    a[i] = a[j]
    a[j] = t

def partition(a, lo, hi):
    #print a[lo:hi+1]
    i, j = lo+1, hi
    while 1:
        while i < hi and a[i] < a[lo]:
            i+=1
        while lo < j and a[lo] < a[j]:
            j-=1
        if i >= j:
            break
        exch(a, i, j)
    exch(a, lo, j)
    #print a[lo:hi+1]
    return j

def partition3way(a, lo, hi):
    #print a[lo:hi+1]
    lt, gt = lo, hi
    i = lo
    m = random.randrange(lo, hi)
    v = a[m]
    while i <= gt:
        c = cmp(a[i], v)
        if c < 0:
            exch(a, lt, i)
            lt += 1
            i += 1
        elif c > 0:
            exch(a, gt, i)
            gt -= 1
        else:
            i += 1
    #print a[lo:hi+1]
    return lt, gt

# kth without duplicated numbers
def kthSmallest(arr, k):
    lo, hi = 0, len(arr)-1
    while lo < hi:
        j = partition(arr, lo, hi)
        if j < k:
            lo = j+1
        elif k < j:
            hi = j-1
        else:
            return arr[j]
    return arr[lo]

def kthSmallestWithDuplicates(arr, k):
    lo, hi = 0, len(arr)-1
    while lo < hi:
        lt, gt = partition3way(arr, lo, hi)
        #print lt, gt, k
        if k < lt:
            hi = lt-1
        elif gt < k:
            lo = gt+1
        else:
            return arr[k]
    return arr[lo]

for i in xrange(5):
    print kthSmallest([1,4,5,3,2], i)
print
for i in xrange(8):
    print kthSmallestWithDuplicates([1,2,3,2,3,3,2,2], i)
