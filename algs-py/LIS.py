import bisect
class Solution(object):

    def longestIncreaseSubsequence(self, arr):
        # n^2, dp
        n = len(arr)
        if n == 0:
            return 0
        lis = [1]*n
        for i in xrange(n):
            for j in xrange(i):
                if arr[i] > arr[j]:
                    lis[i] = max(lis[i], lis[j]+1)
        print lis
        return max(lis) 

    def longestIncreaseSubsequence_nlogn(self, arr):
        # nlogn
        n = len(arr)
        if n == 0:
            return 0
        q = []
        for num in arr:
            if not q or num > q[-1]:
                q.append(num)
            else:
                idx = bisect.bisect_left(q, num)
                q[idx] = num
        print q
        return len(q)

if __name__ == '__main__':
    test = Solution()
    a = [1,3,5,2,4,6,1]
    print test.longestIncreaseSubsequence(a)
    print test.longestIncreaseSubsequence_nlogn(a)
