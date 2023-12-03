'''
Given the sequence of keys visited by a postorder traversal of a binary search tree, reconstruct the tree.

For example, given the sequence 2, 4, 3, 8, 7, 5, you should construct the following tree:

    5
   / \
  3   7
 / \   \
2   4   8
'''
from util.tree import Node

def create_tree(arr):
    n = len(arr)

    if n == 1:
        return Node(arr[0])

    a = Node(arr.pop())
    for i in range(n-2, -2, -1):
        if arr[i] < a.value:
            break
    
    if i > -1:
        a.left = create_tree(arr[:i+1])
    if i < len(arr)-1:
        a.right = create_tree(arr[i+1:])

    return a
        

lst = [2, 4, 3, 8, 7, 5]
print(create_tree(lst))
