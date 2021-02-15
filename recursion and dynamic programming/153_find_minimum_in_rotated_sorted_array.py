'''
Given the sorted rotated array nums, return the minimum element of this array.
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
'''


# this one is similar to #33 search in rotated sorted array.
# you start with typical binary search, and throw away any segments where start index is less than end index
# return the min() of all the start indices of all halved arrays

# this could be refactored to remove the recursive calls and improve speed
#  while left pointer < right pointer
#       take the mid of the array, if the mid is > end, throw out left side by setting left pointer to mid
#       else  start throw out right side by setting right pointer to mid
#       repeat until  the pivot point is found and return the pivot  

class Solution:
    def findMin(self, nums):
        return self.util(nums, 0, len(nums)-1)

    def util(self, nums, start, end):
        if start >= end:
            return nums[start]
        if nums[start] < nums[end]:
            return nums[start]
        mid = (start+end)//2
        return min(self.util(nums, start, mid), self.util(nums, mid+1, end))
