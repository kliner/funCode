
def merge(arr, aux, lo, m, hi):
    for i in xrange(lo, hi+1):
        aux[i] = arr[i]
    i, j = lo, m+1
    for k in xrange(lo, hi+1):
        if i > m:
            arr[k] = aux[j]
            j+=1
        elif j > hi:
            arr[k] = aux[i]
            i+=1
        elif aux[j]<aux[i]:
            arr[k] = aux[j]
            j+=1
        else:
            arr[k] = aux[i]
            i+=1

def divide(arr, aux, lo, hi):
    if lo >= hi:
        return
    m = (lo+hi) >> 1
    divide(arr, aux, lo, m)
    divide(arr, aux, m+1, hi)
    merge(arr, aux, lo, m, hi)
    return arr

a = [4,3,5,3,6,4,2,1]
n = len(a)
aux = [0]*n
print divide(a, aux, 0, n-1)
