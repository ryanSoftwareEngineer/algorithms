'''
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.
'''


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = closeval = 2**31
        for i in range(len(nums)-2):
            val = nums[i]
            left = i+1
            right = len(nums)-1
            while left < right:
                leftval = nums[left]
                rightval = nums[right]
                total = leftval + val + rightval
                if total == target:
                    return target
                elif total < target:
                    left+=1
                else:
                    right-=1
                if abs(total-target) < closest:
                    closest = abs(total-target)
                    closeval = total
        return closeval