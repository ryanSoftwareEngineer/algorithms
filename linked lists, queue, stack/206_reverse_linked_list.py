'''
Reverse a singly linked list.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        if not head:
            return None
        node = head.next
        head.next = None
        while node:
            temp = node.next
            node.next = head
            head = node
            node = temp
        return head
