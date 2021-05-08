'''
https://leetcode.com/problems/first-unique-number/
You have a queue of integers, you need to retrieve the first unique integer in the queue.

Implement the FirstUnique class:

FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
int showFirstUnique() returns the value of the first unique integer of the queue, and returns -1 if there is no such integer.
void add(int value) insert value to the queue.

'''

# I thought of using the hash[key] = node pattern to keep track of the unique elements
# the first element in the list is always the most recent

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = Node(0)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        self.size += 1

    def pop(self, node):
        if self.size == 0:
            return
        node.prev.next = node.next
        node.next.prev = node.prev


class FirstUnique:

    def __init__(self, nums: List[int]):
        self.map = {}
        self.lst = LinkedList()
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        return self.lst.head.next.val

    def add(self, value: int) -> None:
        if value in self.map:
            if self.map[value] == False:
                return
            self.lst.pop(self.map[value])
            self.map[value] = False
            return
        node = Node(value)
        self.lst.add(node)
        self.map[value] = node