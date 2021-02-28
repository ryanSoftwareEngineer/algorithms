'''
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.
Input: n = 5 edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
Output: true.
'''

# store graph in a hash map ... in this case since nodes are labeled from 0 to n-1 we can just use an array to index
# each index will contain a list of connected nodes
# if len(edges) >= n there must be circular dependency return false
# if len(edges) < n-1 then there's missing nodes required to make the tree return false
# do a bfs or dfs and see if any node's are visited twice... if so return false else return true

def graph_valid_tree(n, edges):
    if len(edges) != n-1:
        return False
    map = [[] for _ in range(n)]
    for a, b in edges:
        map[a].append(b)
        map[b].append(a)
    return not dfs(map, edges[0][0], set(), -1)

def dfs(map, node, visited, parent):
    print(node)
    if node in visited:
        return False
    visited.add(node)
    ans = False
    for child in map[node]:
        if child != parent:
            ans = ans or dfs(map, child, visited, node)
    return ans

input = [[0, 1], [0, 2], [0, 3], [1, 4]]
print(graph_valid_tree(5, input))

# output:
# 0
# 1
# 4
# 2
# 3
# True


