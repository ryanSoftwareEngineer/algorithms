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

