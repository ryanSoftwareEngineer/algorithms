'''
Given two sorted arrays nums1 and nums2 of size m and n respectively,
return the median of the two sorted arrays.
'''

# split smaller array
# split the other array where equal length with total of left and right
# if leftside first array <= rightside bottom  and leftside second <= right top :
#  return max of two left sides and min of two right sides
# if top left > right then split to the left side
# else split to right side

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        count = 0
        total = len(nums1) + len(nums2)
        half = (total + 1) // 2
        left = 0
        right = len(nums1) - 1
        while left <= right:
            count += 1
            if count > 10: break;
            mid = (left + right) // 2
            bot = half - mid
            leftx = float(-inf) if mid <= 0 else nums1[mid - 1]
            righty = float(inf) if bot >= len(nums2) else nums2[bot]
            lefty = float(-inf) if bot <= 0 else nums2[bot - 1]
            rightx = float(inf) if mid >= len(nums1) else nums1[mid]
            if leftx <= righty and lefty <= rightx:
                leftmax = max(leftx, lefty)
                rightmin = min(rightx, righty)
                if total % 2 == 1:
                    return leftmax
                else:
                    return (leftmax + rightmin) / 2
            elif leftx > righty:
                right = mid
            else:
                left = mid + 1
        total -= 2
        half = total // 2
        half -= 1
        if total % 2 == 1:
            return nums2[half]
        else:
            return (nums2[half - 1] + nums2[half]) / 2
