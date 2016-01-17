def getSum(T, idx):
    ans = 0
    while idx:
        ans += T[idx]
        idx -= idx & (-idx)
    return ans

def update(T, idx, val):
    while idx <= len(T)-1:
        T[idx] += val
        idx += idx & (-idx)

def count(nums):
    n = len(nums)
    m = max(nums)
    T = [0] * (m+1)
    ans = 0
    for num in nums[::-1]:
        ans += getSum(T, num-1)
        update(T, num, 1)
    print T
    return ans

print count([8,4,2,1])
print count([4,3,2,1])

        
