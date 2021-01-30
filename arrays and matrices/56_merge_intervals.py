'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the
non-overlapping intervals that cover all the intervals in the input.

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
'''

# sort by first value of each pair
#
# if prev[1] >= current[0]
#    current[0] = prev[0] continue
#   else append current
#   update prev to current
class Solution:
    def merge(self, intervals):
        if len(intervals)<2:
            return intervals
        results = []
        # what if you could do it without sort
        intervals.sort(key= lambda x: x[0])
        prev = intervals[0]
        for i in range(1, len(intervals)):
            cur = intervals[i]
            if prev[1]>= cur[0]:
                prev[1]= max(cur[1], prev[1])
                continue
            else:
                results.append(prev)
                prev = cur
        results.append(prev)
        return results

test = [[1,3],[2,6],[8,10],[15,18]]
a = Solution()
a.merge(test)