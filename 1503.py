'''
This problem was asked by Google.

The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

You may also use a list or array to represent a set.
'''

from itertools import combinations

# with itertools import, combine nCi combinations for i in range n
def power_set(s):
   
    power = set()
    for i in range(len(s) + 1):
        for e in combinations(s,i):
            power.add(e)

    return power


# without itertools. power set has 2^n items, for i in range 2^n include set element j if j'th bit of i is set
def power_set_binary(s):
    
    s = list(s)

    power = [[s[j] for j in range(len(s)) if i & 1<<j] for i in range(2**len(s))]
    # power = []
    # for i in range(2**len(s)):
    #     e = []
    #     for j in range(len(s)):
    #         if (i & 1<<j):
    #             e.append(s[j])
    #     power.append(e)

    return power
    

s = {1, 2, 3}
print(power_set_binary(s))