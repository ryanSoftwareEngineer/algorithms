'''
Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
'''
from collections import deque


class Solution:
    # iterate through with nested loop, everytime a 1 is encountered
    # start a bfs or dfs  to set 1's to 0's and increment counter +=1
    def numIslands(self, grid):
        counter = 0
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if col == "1":
                    grid = self.bfs(grid, i, j)
                    counter+=1
        return counter

    def bfs(self, grid, row, col):
        que = deque()
        que.appendleft((row, col))
        while que:
            rw, cl = que.pop()
            if rw < 0 or rw >= len(grid) or cl < 0 or cl >= len(grid[0]) or grid[rw][cl]== '0':
                continue
            grid[rw][cl] = '0'
            que.appendleft((rw+1, cl))
            que.appendleft((rw, cl+1))
            que.appendleft((rw - 1, cl))
            que.appendleft((rw, cl-1))
        return grid

grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
a = Solution()
b= a.numIslands(grid)
print(b)