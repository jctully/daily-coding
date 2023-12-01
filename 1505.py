'''
Given an integer list where each number represents the number of hops you can make, determine whether you can reach to the last index starting at index 0.

For example, [2, 0, 1, 0] returns True while [1, 1, 0, 1] returns False.
'''

# solution I came up with, keep extra array containing whether end can be reached from i, by iterating backwards
#    through arr and checking whether some index that reaches end is reachable. O(n) time and space
def can_reach_end(arr):
    n = len(arr)
    reaches_end = [False]*n
    reaches_end[n-1] = True

    for i in range(n-2, -1, -1):
        if(any(reaches_end[i+1 : i+arr[i]+1])):
            reaches_end[i] = True
    
    return reaches_end[0]


# implementing constant space approach from memory a while after reading about it. keep running variable holding furthest index reachable
def can_reach_end(arr):
    furthest_i = 0

    for i in range(len(arr)):
        if furthest_i < i:
            return False
        furthest_i = max(furthest_i, i + arr[i])
        if furthest_i >= len(arr)-1:
            return True

    return True


lst = [2, 0, 1, 0]
print(can_reach_end(lst))