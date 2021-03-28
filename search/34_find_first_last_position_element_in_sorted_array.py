'''
Given an array of integers nums sorted in ascending order, find the starting
and ending position of a given target value. If target is not found in the array,
return [-1, -1].
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
'''


class Solution:
    def searchRange(self, nums, target):
        a, b = self.search(nums, 0, len(nums) - 1, target, float('inf'), float('-inf'))
        if a == float('inf'):
            return -1, -1
        return a, b

    def search(self, nums, start, end, target, a, b):
        if start > end:
            return a, b
        mid = (start + end) // 2
        if nums[mid] == target:
            a = min(a, mid)
            b = max(b, mid)
        a, b = self.search(nums, start, mid - 1, target, a, b)
        a, b = self.search(nums, mid + 1, end, target, a, b)
        return a, b