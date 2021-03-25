# class node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
#
#     def f(self, node):
#         node = node.next
#
#
# a = node(1)
# b = node(2)
# c = node(3)
# d = node(4)
# e = node(5)
# a.next = b
# b.next = c
# c.next = d
# d.next = e
# def foo(node):
#     node.next = c
#
#
# print(a.next.val)
# g =a
# foo(g)
# print(a.next.val)
#
# a.f(g)
# print(a.next.val)
# d = a


def f(a):
    a = 4
    return a

a = None
b = None
c = a or b
print(c)