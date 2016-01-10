# Find the missing number in the increasing sequence. i.e. :
# input: 1 2 3 5 6 7 output: 4

# binary search, O(logn)
def find(arr, lo, hi):
    if not arr:
        return 0
    if lo == hi and arr[lo] == lo+1:
        return lo + 2
    if lo == hi and arr[lo] != lo+1:
        return lo
    m = (lo + hi) >> 1
    if arr[m] == m+1: # a[3] = 4, target is in [5:]
        if m+1 == len(arr):
            return m+1
        if arr[m+1] == m+3:
            return m+2
        return find(arr, m+1, hi)
    else: # a[3] = 5, target is in [:4]
        if m == 0:
            return 1
        if arr[m-1] == m+1:
            return m
        return find(arr, lo, m-1)
    
a = [1,2,3,5,6,7]
print find(a, 0, len(a)-1)
a = []
print find(a, 0, len(a)-1)
a = [2,3,4]
print find(a, 0, len(a)-1)
a = [1,2,3]
print find(a, 0, len(a)-1)
