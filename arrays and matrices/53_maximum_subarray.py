'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''

# the divide and conquer approach is technically slower than kadane's but it's helpful fr learning the d&c design paradigm

def max_sub(nums):
    


class Solution(object):
    '''
    iterate through array
    keep track of sum so far
    if sum_so_far < 0
     reset sum
    if sum_so_far > sum_max
        update sum
    '''
    def maxSubArray(self, nums):
        if len(nums)<1:
            return 0
        sum_so_far = 0
        sum_max = nums[0]
        for i in nums:
            sum_so_far += i
            if sum_so_far < 0:
                sum_so_far= 0
            if (sum_so_far > sum_max and sum_so_far != 0):
                sum_max = sum_so_far
            if i > sum_max:
                sum_max = i
        return sum_max


nums = [-2, -1]
a = Solution()
b =a.maxSubArray(nums)
print(b)


