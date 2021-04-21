'''

https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/

Given a rectangular cake with height h and width w, and two arrays of integers horizontalCuts and verticalCuts where horizontalCuts[i] is the distance from the top of the rectangular cake to the ith horizontal cut and similarly, verticalCuts[j] is the distance from the left of the rectangular cake to the jth vertical cut.

Return the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the arrays horizontalCuts and verticalCuts. Since the answer can be a huge number, return this modulo 10^9 + 7.
'''
# a better solution is simply to keep track of max height and max width of cuts
#

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        maxheight = currentheight = 0
        for i in horizontalCuts:
            maxheight = max(maxheight, i-currentheight)
            currentheight = i
        maxheight = max(maxheight, h-horizontalCuts[-1])
        maxwidth = currentwidth = 0
        for i in verticalCuts:
            maxwidth = max(maxwidth, i-currentwidth)
            currentwidth = i
        maxwidth = max(maxwidth, w-verticalCuts[-1])
        return (maxheight *maxwidth) % ((10**9)+7)

# first attempt. I used a dynamic progamming algorithm to iterate through h*w and keep track of max width* height but
# this is not efficient enough
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        row_cuts = set(horizontalCuts)
        col_cuts = set(verticalCuts)
        dp = [0]* w
        max_so_far = 0
        for row in range(h):
            counter = 0
            for col in range(w):
                if col in col_cuts:
                    counter = 0
                if row in row_cuts:
                    dp[col] =0
                counter+=1
                dp[col]+=1
                max_so_far = max(max_so_far, (counter* dp[col]))
        return max_so_far