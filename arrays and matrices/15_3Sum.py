'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.
Notice that the solution set must not contain duplicate triplets.
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
'''


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        ans = []
        i = 0
        while i < len(nums) - 2:
            left = i + 1
            right = len(nums) - 1
            while left < right:
                temp = nums[left] + nums[right] + nums[i]
                if temp == 0:
                    ans.append([nums[left], nums[right], nums[i]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif temp < 0:
                    left += 1
                else:
                    right -= 1
            while i < len(nums) - 2 and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        return ans
