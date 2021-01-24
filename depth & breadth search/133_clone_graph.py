'''
Given a reference of a node in a connected undirected graph.
Return a deep copy (clone) of the graph.

Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
'''
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution(object):
    def cloneGraph(self, node):
        if Node is None:
            return None
        return self.clone_util(node, {})

    def clone_util(self, node, visited):
        if node is None:
            return
        if node.val in visited:
            return visited[node.val]
        new_node = Node(node.val)
        visited[node.val] = new_node
        for neighbor in node.neighbors:
                cloned_node = self.clone_util(neighbor, visited)
                new_node.neighbors.append(cloned_node)
        return new_node

''' 
The input format for leetcode is in the form [[2,4],[1,3],[2,4],[1,3]]
but the output wanted is a node.
The output of this graph is 
{
1: [2, 4],
2: [1, 3],
3: [2, 4],
4: [1, 4],
}

'''