'''
Given an integer array nums, return the length of the longest strictly increasing subsequence.
A subsequence is a sequence that can be derived from an array by deleting some or no elements without
hanging the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

Could you come up with the O(n2) solution?
Could you improve it to O(n log(n)) time complexity?
'''

# create stack and counter
# iterate through array for each iteration iterate again
# if current number > stack[-1]
#    add item to stack, increment counter
# else: pop until empty decrement for each pop until
# return max_so_far
#  you could run this for each element... this would be o(n2)... how can I get the o(nlogn) solution ?
from collections import deque

# set dp = same length as nums initialize to 1
# for every i ... then for every j in 0 to i
# if nums[i] is greater than nums[j]... then you know that i must have +1 more than j
# take the highest of all j's to i... then add 1 for i
class Solution:
    def lengthOfLIS(self, nums):
        dp = [1]* len(nums)
        dp[0]= 1
        max_so_far = 1
        for a in range(1, len(nums)):
            for b in range(0, a):
                if nums[a] > nums[b]:
                    dp[a] = max(dp[b]+1, dp[a])
            max_so_far = max(max_so_far, dp[a])
        print(dp)
        return max_so_far
a= Solution()
input = [10,9,2,5,3,7,101,18]

b = a.lengthOfLIS(input);
print(b)