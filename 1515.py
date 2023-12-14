'''
medium:
This problem was asked by Twitter.

Given a list of numbers, create an algorithm that arranges them in order to form the largest possible integer. 
For example, given [10, 7, 76, 415], you should return 77641510.
'''

# sort nums in reverse lexicographical order. To deal with ex. 78 > 7 > 76, pad numbers out with first digit when comparing.
def sort_ints(nums: list):
    m = len(str(max(nums)))

    def key(num):
        num = str(num)
        while len(num) < m:
            num += num[0]
        return num

    nums.sort(key = key, reverse=True)
    
    print(nums)
    return int("".join([str(n) for n in nums]))


nums = [10, 7, 76, 415, 78, 1]
print(sort_ints(nums))