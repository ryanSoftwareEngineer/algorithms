'''
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by
continuously following the next pointer. Internally, pos is used to denote the index of the node that
tail's next pointer is connected to. Note that pos is not passed as a parameter.
'''



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# first thought was iterate and store in hash set then if two are found or end is reached then return true/false
# a solution without extra memory would be using two pointers, which seems to be the main solution so I decided to go with that
class Solution:
    def hasCycle(self, head):
        if not head:
            return False
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False