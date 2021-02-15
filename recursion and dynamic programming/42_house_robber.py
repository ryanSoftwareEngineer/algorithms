'''You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it
will automatically contact the police if two adjacent houses were broken into on the same night.
Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of
money you can rob tonight without alerting the police.
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
'''

# f(n) = max( f(n-3) + f(n), f(n-2) + f(n)
class Solution:
    def rob(self, nums):
        if not nums: return 0
        if len(nums) <2:
            return nums[0]
        if len(nums)==2:
            return max(nums[0], nums[1])
        nums[2] = nums[0]+ nums[2]
        result = max(nums[2], nums[1])
        for i in range(3, len(nums)):
            nums[i] = max((nums[i-3]+nums[i]), nums[i-2]+ nums[i])
            result = max(nums[i], result)
        return result

a= Solution()
b = [1,2,3, 5]
print(a.rob(b))