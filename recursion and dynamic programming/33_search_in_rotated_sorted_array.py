'''
You are given an integer array nums sorted in ascending order (with distinct values), and an integer target.
Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
If target is found in the array return its index, otherwise, return -1.

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
'''

'''
cut array in half 
if start < end and target > end ( target is not in this section, toss it )
else split until mid is found
'''

class Solution(object):
    def search(self, nums, target):
        return self.__search_util(nums, 0, len(nums)-1, target)
    def __search_util(self, nums, start, end, target):
        if start > end:
            return -1
        if nums[start] < nums[end] and (target > nums[end] or target < nums[start]):
            return -1
        mid = (start+end)//2
        if nums[mid] == target:
            return mid
        else:
            one = self.__search_util(nums, start, mid-1, target)
            two = self.__search_util(nums, mid+1, end, target)
            return max(one, two)


a = Solution()
nums = [4,5,6,7,0,1,2]
target = 0
print(a.search(nums, target))

'''
output: 4
'''