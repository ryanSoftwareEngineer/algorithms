'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''

# the divide and conquer approach is technically slower than kadane's but it's helpful fr learning the d&c design paradigm

def max_sub(nums, start, end ):
    if start == end:
        return nums[start]
    mid = (start+end)//2
    left_max = max_sub(nums, start, mid)
    right_max = max_sub(nums, mid+1, end)
    cross_max = cross(nums, start, mid, end)
    return max(left_max, right_max, cross_max)

def cross(nums, start, mid, end):
    left = right = -2**32
    sum1 = sum2 =0
    for i in range(mid, start-1, -1):
        sum1+=nums[i]
        if sum1 > left:
            left = sum1
    for j in range(mid+1, end+1):
        sum2+=nums[j]
        if sum2 > right:
            right = sum2
    print(start, end, left, right, max(left, right, left+right))
    return max(left, right, left+right)

nums = [-2,-5, 6, -2, -3, 1, 5, -6]
print(max_sub(nums, 0, len(nums)-1))

# outputs 3,1,2 so max is 3,  3 is max of [2,-1,3,-2] and 2 is max of [3,-2,1,-2]

class Solution(object):
    # iterate through array
    # keep track of sum so far
    # if sum_so_far < 0
    #  reset sum
    # if sum_so_far > sum_max
    #     update sum
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

#
# nums = [-2, -1]
# a = Solution()
# b =a.maxSubArray(nums)
# print(b)


