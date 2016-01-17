# two sorted array, from each choose one num, calc total count which sum >= query
# [3,5,6], [4,9], 9
# return 2

def solve(arr1, arr2, q):
    l1, l2 = len(arr1), len(arr2)
    i, j = 0, l2
    ans = 0
    while i < l1 and j > 0:
        print i, j
        if arr1[i] + arr2[j-1] >= q:
            j-=1
        else:
            ans += (l2-j)
            i+=1
    ans += (l1-i)*l2
    return ans

print solve([3,5,6], [4,9], 9)
print solve([1,1,1,1,1,1,1,1,1,1], [1,1,1,1,1,1,1,1,1,1], 9)
print solve([1,1,1,1,1,1,1,1,1,1], [1,1,1,1,1,1,1,1,1,1], 2)


# two sorted array, from each choose one num, calc total count which sum >= lower and sum <= upper
# [3,5,6], [4,9], 8, 10
# [1,2,3,5,6], [4,5,6,7,8,9], 8, 10
# return 2
a,b,lo,hi = [1,2,3,5,6], [4,5,6,7,8,9], 8, 10
print solve(a, b, lo) - solve(a, b, hi+1)
