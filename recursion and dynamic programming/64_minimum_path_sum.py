'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right,
which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
'''

# one could run this in place w/o using the extra result grid or arrays
# such that grid[i][j] += min(grid[i-1][j], grid[i][j-1]) but I'm trying to relate to #62 unique paths problem
def minPathSum2(grid):
    row =len(grid)
    col = len(grid[0])
    result = [grid[0][0]]* col
    row_result = [grid[0][0]]* row
    for i in range(1, row):
        row_result[i] = row_result[i-1] +grid[i][0]
    for j in range(1, col):
        result[j] = result[j-1]+ grid[0][j]
    print(result, row_result)
    for a in range(1, row):
        result[0]= row_result[a]
        for b in range(1, col):
            grid_value = grid[a][b]
            print(a, b, result[b], result[b-1])
            result[b] = min(result[b], result[b-1]) + grid_value
    print(result)
    return result

grid = [[1,2,3],
        [4,5,6]]
minPathSum2(grid)
# output:
# [1, 3, 6] [1, 5]
# 1 1 3 5
# 1 2 6 8
# [5, 8, 12]

# below is  brute force using back tracking.. we could use memoization to reduce from 2^n to polynomial
#  we also don't need paths but I like to print out the path
def minPathSum( grid, row, col, sum, mini, path):
        if row <0 or col <0:
            return mini
        path.append(grid[row][col])
        if row == 0 and col == 0:
            if sum < mini:
                mini = sum
            path.pop()
            return mini
        sum += grid[row][col]
        a= min(minPathSum(grid, row-1, col, sum, mini, path), minPathSum(grid, row, col-1, sum, mini, path))
        path.pop()
        return a
# grid = [[1,3,1],[1,5,1],[4,2,1]]
# print(minPathSum(grid, len(grid)-1, len(grid[0])-1, grid[0][0], 2**32, [] ))
