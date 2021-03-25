''''
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums
such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
Notice that the solution set must not contain duplicate quadruplets.
'''

# esentially wrap it around 3sum multiplying by o(n) complexity
class Solution:
    def fourSum(self, nums, target):
        if len(nums) < 4:
            return []
        nums.sort()
        final = []
        i = 0
        while i < len(nums) - 3:
            temp = self.threesum(nums[i + 1:], target - nums[i])
            if temp:
                for a in temp:
                    final.append([nums[i], a[0], a[1], a[2]])
                i += 1
                while i < len(nums) - 3 and nums[i] == nums[i - 1]:
                    i += 1
                continue
            i += 1
        return final

    def threesum(self, nums, target):
        ans = []
        i = 0
        while i < len(nums) - 2:
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[left] + nums[right] + nums[i]
                if total == target:
                    ans.append([nums[left], nums[right], nums[i]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
            while i < len(nums) - 2 and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        return ans