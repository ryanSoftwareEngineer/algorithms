'''Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two
lines, which, together with the x-axis forms a container, such that the container contains the most water.
'''

# brute force would be to simply do a nested loop checking every possible combination at each index
# the wider it is the better unless the height > width .. so to sacrifice width we have to seek out
# the tallest branches
class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_so_far = self.getArea(left, right, height)
        while left < right:
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
            temp = self.getArea(left, right, height)
            max_so_far = max(max_so_far, temp)
        return max_so_far

    def getArea(self, a, b, height):
        return (b - a) * (min(height[a], height[b]))