'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
Now consider if some obstacles are added to the grids. How many unique paths would there be?
An obstacle and space is marked as 1 and 0 respectively in the grid.

https://leetcode.com/problems/unique-paths-ii/
'''


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        temp_array = [1 for _ in range(len(obstacleGrid[0]))]
        bit = 0
        i = 0
        while i < len(obstacleGrid[0]) - 1:
            i += 1
            if obstacleGrid[0][i] == 1:
                bit = 1
            if bit == 1:
                temp_array[i] = 0
        for i in range(1, len(obstacleGrid)):
            row = obstacleGrid[i]
            for j in range(len(row)):
                if row[j] == 1:
                    temp_array[j] = 0
                elif j == 0:
                    if obstacleGrid[i - 1][0] == 0 and temp_array[0] == 1:
                        temp_array[0] = 1
                    else:
                        temp_array[0] = 0
                else:
                    temp_array[j] = temp_array[j] + temp_array[j - 1]
        return temp_array[-1]



