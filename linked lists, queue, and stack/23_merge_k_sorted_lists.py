'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
'''

# my approach was the divide and conquer approach
# I would merge pairs lists[i] and lists[i+1] into just list[i]
# then I would swap the emptied i to the end of the list and pop it
class Solution(object):
    def mergeKLists(self, lists):
        if len(lists) < 1:
            return

        def mergetwo(a, b):
            root = pointer = ListNode()
            while a or b:
                if a and b:
                    if a.val < b.val:
                        pointer.next = a
                        pointer = a
                        a = a.next

                    else:
                        pointer.next = b
                        pointer = b
                        b = b.next
                else:
                    pointer.next = a or b
                    break
            return root.next

        i = 0
        while len(lists) > 1:
            if i >= len(lists) - 1:
                i = 0
            lists[i] = mergetwo(lists[i], lists[i + 1])
            lists[i + 1], lists[-1] = lists[-1], lists[i + 1]
            lists.pop()
            i += 1
        return lists[0]
