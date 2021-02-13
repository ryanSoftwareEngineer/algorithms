'''Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.'''

'2 -3 -1 2 0 2'
# min: 2 -6 -1 -2 0 2
# max: 2 -6 -1 -2 0 0

class Solution:
    def maxProduct(self, nums):
        if not nums:
            return 0
        mini = maxi = max_so_far = nums[0]
        for num in nums[1:]:
            if num > 0:
                maxi = max(num, maxi*num)
                mini = min(num, mini*num)
            else:
                temp = maxi
                maxi = max(num, mini*num)
                mini = min(num, temp*num)
            max_so_far = max(maxi, max_so_far)
            print(mini, maxi)
        return max_so_far

input =  [2,-3,-1,2,0,2, -2, 2, ]
a = Solution()
print(a.maxProduct(input))

