'''
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
(i.e., from left to right, then right to left for the next level and alternate between).

Example:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
'''

# intuition would tell you to use a BFS. I imeplented a bfs using two stacks so that I could iterate backwards
# for child in children: append child to stack a
# then for all nodes in stack a append their children to stack b

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        reverse = True
        stacka = deque()
        stackb = deque()
        stacka.append(root)
        answer = []
        while stacka or stackb:
            temparr = []
            reverse = not reverse
            if stacka:
                while stacka:
                    node = stacka.pop()
                    temparr.append(node.val)
                    if node.left:
                        stackb.append(node.left)
                    if node.right:
                        stackb.append(node.right)
            else:
                while stackb:
                    node = stackb.pop()
                    temparr.append(node.val)
                    if node.right:
                        stacka.append(node.right)
                    if node.left:
                        stacka.append(node.left)

            answer.append(temparr)
        return answer