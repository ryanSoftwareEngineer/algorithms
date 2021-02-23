'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed.
All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile,
adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses
were broken into on the same night.

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
'''


class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums)<4:
            return max([i for i in nums])
        return max(self.__rob(nums[1:]), self.__rob(nums[:-1]))
        # return self.__rob(nums)

    def __rob(self, nums):
        prev = cur = 0
        for n in nums:
            temp = cur
            cur = max(cur, (prev+n))
            prev = temp
        return cur




nums = [1,2,3,1,2,6]
a = Solution()
print(a.rob(nums))