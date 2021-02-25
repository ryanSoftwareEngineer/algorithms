'''
#1
Given an array of meeting time intervals consisting of start and end times [s1, e1], [s2, e2], ... , determine if a person could attend all meetings.
For example,
Given [ [0, 30], [5, 10], [15, 20] ],
return false.

#2
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
'''



def meeting_rooms_i(intervals):
    intervals.sort( key= lambda x:x[0])
    prev = 0
    for start, end in intervals:
        if start < prev:
            return False
        prev = end
    return True


# intervals = [[7, 9], [1, 4], [8, 20]]
# print(meeting_rooms(intervals))