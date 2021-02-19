'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array
prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
'''

class Solution:
    def canFinish(self, numCourses, prerequisites):
        if len(prerequisites)==0:
            return True
        graph =[[] for i in range(numCourses)]
        visited = [None for i in range(numCourses)]
        for req, course in prerequisites:
            graph[req].append(course)

        for i in range(numCourses):
            if not self.dfs(graph, visited, i):
                return False
        return True

    def dfs(self, graph, visited, node):
        # print(graph, visited, node)
        if visited[node] is not None:
            return visited[node]
        visited[node] = False
        for i in graph[node]:
            if not self.dfs(graph, visited, i):
                return False
        visited[node] = True
        return True




prerequisites = [[0,2],[1,2],[1,0]]
numCourses = 3
a = Solution()
print(a.canFinish(numCourses, prerequisites))
# outputs true

