'''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
'''


class Solution:
    # The code could be a lot easier to read if this was done in two passes,
    # you could iterate through first to insert the newinterval
    # then iterate again to merge

    #  I wanted to try doing this in one pass though for fun
    def insert(self, intervals, newInterval):
        if len(intervals)< 1:
            return [newInterval]
        results = []
        prev = intervals[0]
        if prev[0] > newInterval[0]:
            prev = newInterval
        for i, cur in enumerate(intervals):
            temp = prev
            if prev[1]< cur[0]:
                results.append(prev)
                prev = cur
            prev = self.merge(prev, cur)
            prev = self.merge(prev, newInterval)
            if temp[1]< newInterval[0] and newInterval[1] < cur[0]:
                results.append(newInterval)
        results.append(prev)
        if newInterval[0]> prev[1]:
            results.append(newInterval)
        return results


    def merge(self, prev, current):
        if prev[1] < current[0] or prev[0]> current[1]:
            return prev
        prev[1] = max(prev[1], current[1])
        prev[0] = min(prev[0], current[0])
        return prev




intervals = [[1,3],[6,15]]
new = [4, 5]
a = Solution()
a.insert(intervals, new)
