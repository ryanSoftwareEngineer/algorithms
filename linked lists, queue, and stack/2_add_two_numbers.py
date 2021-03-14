'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry_over = 0
        root = ListNode(0)
        ans = root
        while l1 or l2:
            root.next = ListNode(getattr(l1, 'val', 0) + getattr(l2, 'val', 0))
            root = root.next
            root.val += carry_over
            carry_over = 0
            if root.val > 9:
                root.val %= 10
                carry_over =1
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry_over == 1:
            root.next = ListNode(1)
        return ans.next