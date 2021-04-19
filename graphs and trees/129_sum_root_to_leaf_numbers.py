'''
https://leetcode.com/problems/sum-root-to-leaf-numbers/

You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers.

A leaf node is a node with no children.
'''


# if converting to str to get int is not allowed tou could create another function
# to iterate through path backwards and sum each element[i] * (10^i or 1) so 1,2,3 -> 3 *1 + 2*10 + 1*100 ...
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def helper(node, path, answers):
            if node is None:
                return answers
            if node.left == None and node.right == None:
                path.append(str(node.val))
                answers += int(''.join(path))
                path.pop()
                return answers
            path.append(str(node.val))
            answers = helper(node.left, path, answers)
            answers = helper(node.right, path, answers)
            path.pop()
            return answers

        return helper(root, [], 0)

