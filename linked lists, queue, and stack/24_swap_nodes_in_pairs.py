'''
Given a linked list, swap every two adjacent nodes and return its head.

Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        ans = prev = ListNode(0)
        pointer = head
        while pointer and pointer.next:
            temp = pointer.next.next
            left = pointer
            right = pointer.next
            right.next = left
            prev.next = right
            prev = left
            pointer = temp
        prev.next = pointer
        return ans.next