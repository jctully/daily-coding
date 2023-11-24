
'''This problem was asked by Facebook.

A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.'''

def paint_houses(arr):
    
    def min_cost(n, k, cost):
        if n == len(arr):
            return cost
        best_cost = float('inf')
        for col in range(len(arr[0])):
            if col != k:
                cost = min_cost(n+1, col, cost + arr[n][col])
                best_cost = min(best_cost, cost)
        return best_cost

    ret = float('inf')
    for col in range(len(arr[0])):
        ret = min(ret, min_cost(0,col,0))
    return ret


arr = [[5,5,5], [100,101,102], [10,150,200]]
print(paint_houses(arr))