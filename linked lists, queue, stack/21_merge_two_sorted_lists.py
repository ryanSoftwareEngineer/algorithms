# Definition for singly-linked list.
'''
Merge two sorted linked lists and return it as a sorted list. The list should be made by
splicing together the nodes of the first two lists.
'''
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        prev = start = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                prev.next = l1
                l1 = l1.next
                prev = prev.next
            else:
                prev.next = l2
                l2 = l2.next
                prev = prev.next
        prev.next = l1 or l2
        return start.next



def create(arr):
    prev = start = ListNode(0)
    for i in arr:
        a = ListNode(i)
        prev.next = ListNode(i)
        prev = prev.next
    return start.next

one = [1,4,5,6,8, 10, 11, 12]
two = [3, 4, 6, 9]
a = create(one)
b = create(two)
c = Solution()
d = c.mergeTwoLists(a, b)
while d:
    print(d.val, end = " ")
    d = d.next

'''
outputs: 1 3 4 4 5 6 6 8 9
'''