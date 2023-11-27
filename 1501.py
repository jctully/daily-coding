'''
This problem was asked by Apple.

Given the root of a binary tree, find the most frequent subtree sum. The subtree sum of a node is the sum of all values under a node, including the node itself.

For example, given the following tree:

  5
 / \
2  -5
Return 2 as it occurs twice: once as the left leaf, and once as the sum of 2 + 5 - 5.
'''


from collections import Counter

class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.val = data
    
def most_frequent_sub(root):
   counts = Counter()

   def subtree_sum(root):
      if not root:
         return 0
      
      left_sum = subtree_sum(root.left)
      right_sum = subtree_sum(root.right)
      sum = left_sum + right_sum + root.val
      
      counts[sum] += 1
      return sum
   
   subtree_sum(root)
   return counts.most_common(1)[0][0]

a = Node(5)
b = Node(2)
c = Node(-5)

a.left = b
a.right = c

print(most_frequent_sub(a))