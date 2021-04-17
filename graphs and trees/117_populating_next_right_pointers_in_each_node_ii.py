'''
https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.
'''

# similar to the last problem we traverse preorder seting the child nodes pointer to the next available node
# from the same level. I created the get_next helper function to find the next node for that level
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def helper(node):
            if node is None:
                return
            if node.left:
                if node.right:
                    node.left.next = node.right
                else:
                    node.left.next = get_next(node)
            if node.right:
                node.right.next = get_next(node)
            helper(node.left)
            helper(node.right)
            return node

        def get_next(node):
            tmp = node
            while tmp.next:
                tmp = tmp.next
                if tmp.left:
                    return tmp.left
                if tmp.right:
                    return tmp.right
            return None

        return helper(root)