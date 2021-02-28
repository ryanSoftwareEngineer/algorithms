'''
#1
Given an array of meeting time intervals consisting of start and end times [s1, e1], [s2, e2], ... , determine if a person could attend all meetings.

#2
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
'''

# number 2:
# sort then iterate through intervals
# at each start time check it against priority queue's front item
# if it is delete that item, add the ending time to queue
# if qsize > max_so_far , update max_so_far
# return max_so_far
#
from queue import PriorityQueue

def meeting_rooms_ii(intervals):
    que = PriorityQueue()
    intervals.sort(key=lambda a: a[0])
    max_so_far = 0
    que.put(intervals[0][1])
    for a,b in intervals[1:]:
        if que.qsize() > max_so_far:
            max_so_far = que.qsize()
        if a > que.queue[0]:
            que.get()
        que.put(b)
    return max_so_far



def meeting_rooms_i(intervals):
    intervals.sort( key= lambda x:x[0])
    prev = 0
    for start, end in intervals:
        if start < prev:
            return False
        prev = end
    return True


intervals = [[1,4], [2, 3], [5,9],[3,7],[4,5],[3,6]]
print(meeting_rooms_ii(intervals))
# output: 4