'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.
Follow up: Could you do this in one pass?
'''


class Solution:
    def removeNthFromEnd(self, head, n):
        answer = fast = head
        counter = 0
        while fast:
            if counter < n:
                fast = fast.next
                counter+=1
                continue
            if fast.next is None:
                head.next = head.next.next
                return answer
            fast = fast.next
            head = head.next
        # if n == length, remove first element
        return answer.next