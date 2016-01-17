# http://www.practice.geeksforgeeks.org/problem-page.php?pid=265
def sort(a, aux, lo, hi):
    if hi <= lo:
        return
    mid = (hi + lo) >> 1
    sort(a, aux, lo, mid)
    sort(a, aux, mid+1, hi)
    merge(a, aux, lo, mid, hi)


def merge(a, aux, lo, mid, hi):
    for i in xrange(lo, hi+1):
        aux[i] = a[i]
    i, j = lo, mid+1
    for k in xrange(lo, hi+1):
        if i > mid:
            a[k] = aux[j]
            j+=1
        elif j > hi:
            a[k] = aux[i]
            i+=1
        elif aux[i] > aux[j]:
            a[k] = aux[j]
            j+=1
        else:
            a[k] = aux[i]
            i+=1

def sysSort(a):
    a.sort()
 
# Input number of test cases
t = int(raw_input())
 
# One by one run for all input test cases
for i in range(0,t):
    arr = []
 
    # Input the size of the array
    n = int(raw_input())
 
    # Input the array
    for x in raw_input().split():
        arr.append(int(x))
 
    #aux = [0] * n
    #sort(arr, aux, 0, n-1)
    sysSort(arr)
    print(arr)

