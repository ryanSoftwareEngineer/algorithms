'''
https://leetcode.com/problems/lfu-cache/
Share
Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:

LFUCache(int capacity) Initializes the object with the capacity of the data structure.
int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.
To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.

When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or put operation is called on it.
'''

# intuition is to use a priority queue to keep track of frequency counts... the problem I had with this
# is updating a frequency count you have to keep the heap maintained

# if we keep a list of nodes and a list of doubly linked lists for each frequency
# then whenever update a frequency we can just pop the node from a lower frequency linked list to a higher
# frequency linked list

from collections import defaultdict


class Node:
    def __init__(self, key=None, val=None, freq=None):
        self.key = key
        self.val = val
        self.freq = freq
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.freq = 1
        self.size = 0
        self.head = Node(None, None, None)
        self.tail = Node(None, None, None)

    def pop(self, node=None):
        if self.size == 0:
            return
        if node == None:
            node = self.tail.prev
        left = node.prev
        right = node.next
        left.next = right
        right.prev = left
        self.size -= 1
        return node

    def add(self, node):

        if self.size == 0:
            self.tail.prev = node
            self.head.next = node
            node.next = self.tail
            node.prev = self.head
            self.size += 1
        else:
            node.next = self.head.next
            node.prev = self.head
            self.head.next.prev = node
            self.head.next = node
            self.size += 1


class LFUCache:
    def __init__(self, capacity: int):
        self.nodes = defaultdict(list)
        self.lists = defaultdict(LinkedList)
        self.lfu = 1
        self.size = 0
        self.capacity = capacity

    def _update(self, key):
        #  when we need update freq of key we pop it from
        # the linked list where frequency == the node's current frequency
        # we increase the frequency by one and append it to the linked list of frequency+1
        # if the frequency is the same as our least frequently used count
        #       then we check if that linked list at that least frequency is empty
        #        if it empty we need to increase our least frequency by 1

        node = self.nodes[key]
        freq = node.freq
        self.lists[freq].pop(node)
        if freq == self.lfu and self.lists[freq].size == 0:
            self.lfu += 1
        node.freq += 1
        self.lists[freq + 1].add(node)

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        self._update(key)
        return self.nodes[key].val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.nodes:
            self.nodes[key].val = value
            self._update(key)
            return
        # if self.size == 0:
        #     self.lists[1] = LinkedList()
        #     self.lists[1].add(Node(key, value, 1))
        #     self.size+=1
        #     return

        if self.capacity == self.size:
            #             pop from self.lists of minused
            nd = self.lists[self.lfu].pop()
            self.nodes.pop(nd.key)
            self.size -= 1

        if 1 not in self.lists:
            self.lists[1] = LinkedList()
        newnode = Node(key, value, 1)
        self.lists[1].add(newnode)
        self.nodes[key] = newnode
        self.lfu = 1
        self.size += 1