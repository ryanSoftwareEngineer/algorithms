'''
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.
You can assume that you can always reach the last index.

so why does jump game 2 come before jump game 1 on leetcode ... it's out of order I don't like that >_>
'''

# as you iterate through nums keep track of the farthest location you can jump at each phase
#    farthest = the max of the current farthest or i+nums[i]
# Every time we reach a target, that starts at zero, we set our new jump target to the current farthest
# we calculate new farthest's from our current position to the new target
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        jumps = target = far =0
        for i in range(len(nums)-1):
            far = max(far, i+nums[i])
            if i == target:
                jumps+=1
                target = far
            if target >= len(nums)-1:
                return jumps
