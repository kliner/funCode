# find least common ancestor

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# 3 travelsal, O(n)+ mem O(n)
def findLCA(root, n1, n2):

    def findPath(root, n):
        if not root:
            return
        if root.val == n:
            return [n]
        left = findPath(root.left, n)
        if left:
            return [root.val] + left
        right = findPath(root.right, n)
        if right:
            return [root.val] + right

    p1 = findPath(root, n1)
    p2 = findPath(root, n2)
    if not p1 or not p2:
        return None
    ans = None
    for i in xrange(min(len(p1), len(p2))):
        if p1[i] != p2[i]:
            return ans
        ans = p1[i]
    return ans

# one travelsal, O(n) + mem O(1)
def findLCA2(root, n1, n2):

    def find(root, n1, n2, marked):
        if not root:
            return
        if root.val == n1:
            marked[0] = 1
            return root.val
        if root.val == n2:
            marked[1] = 1
            return root.val
        left = find(root.left, n1, n2, marked)
        right = find(root.right, n1, n2, marked)
        if left and right:
            return root.val
        if left:
            return left
        if right:
            return right 

    def findOne(root, n):
        if not root:
            return
        if root.val == n or findOne(root.left, n) or findOne(root.right, n):
            return 1
        
    marked = [0,0]
    ans = find(root, n1, n2, marked)
    if marked[0] and marked[1] or (marked[0] and findOne(root, n2)) or (marked[1] and findOne(root, n1)):
        return ans 
    else:
        return 





root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print findLCA(root, 4, 5)
print findLCA(root, 4, 6)
print findLCA(root, 4, 3)
print findLCA(root, 4, 2)
print findLCA(root, 4, 10)
print '-----------'

print findLCA2(root, 4, 5)
print findLCA2(root, 4, 6)
print findLCA2(root, 4, 3)
print findLCA2(root, 4, 2)
print findLCA2(root, 4, 10)
print '-----------'
