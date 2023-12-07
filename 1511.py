'''
This problem was asked by Google.

Given a binary search tree and a range [a, b] (inclusive), return the sum of the elements of the binary search tree within the range.

For example, given the following tree:

    5
   / \
  3   8
 / \ / \
2  4 6  10
and the range [4, 9], return 23 (5 + 4 + 6 + 8).
'''
from util.tree import Node

# traverse the tree recursively based on node's value relative to the range
def tree_sum(root: Node, lo, hi):

    if not root:
        return 0

    sum = 0
    if root.value < lo:
        sum += tree_sum(root.right, lo, hi)
    elif root.value == lo:
        sum += root.value
        sum += tree_sum(root.right, lo, hi)
    elif lo < root.value < hi:
        sum += root.value
        sum += tree_sum(root.left, lo, hi)
        sum += tree_sum(root.right, lo, hi)
    elif root.value == hi:
        sum += root.value
        sum += tree_sum(root.left, lo, hi)
    elif root.value > hi:
        sum += tree_sum(root.left, lo, hi)

    return sum


a = Node(5)
b = Node(3)
c = Node(8)
d = Node(2)
e = Node(4)
f = Node(6)
g = Node(10)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g

print(tree_sum(a, 4, 9))