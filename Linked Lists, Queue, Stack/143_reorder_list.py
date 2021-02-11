'''Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
You may not modify the values in the list's nodes, only nodes itself may be changed.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# my first thought was to loop through once, get the length and double link the list
# then iterate from end points to middle deleting the extra links along the way

# I thought looping through with two pointers to get mid, then adding pointers on a stack after mid

# a solution i looked up would have you reverse the 2nd half instead of using stack...

# thought about using recursion to pass in the start of the list and iterating next for 2nd parameter
# when you get to the end and your popping back up you return head.next to iterate from start while popping back from Ln -> ln-mid
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head) -> None:
        if not head:
            return None
        start = mid = end = head
        end = end.next
        while end and end.next:
            mid, end = mid.next, end.next.next
        end = mid.next
        prev = mid
        while end:
            temp = end.next
            end.next = prev
            prev = end
            end = temp
        end = prev
        while start != mid:
            temp = start.next
            temp2 = end.next
            start.next = end
            end.next = temp
            start = temp
            end = temp2
        end.next = None
        return head

def printll(root):
    i = 1
    while root and i <8 :
        print(root.val)
        root = root.next
        i+=1
a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)
a.next.next.next = ListNode(4)
a.next.next.next.next = ListNode(5)
b= Solution()
printll(b.reorderList(a))
