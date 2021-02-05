'''
Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
'''
# first idea is to store two  arrays of columns and rows to be set to zero
# 2nd idea is to use first row and first columns as arrays to hold boolean values of whether this row should change or not
class Solution:
    def setZeroes(self, matrix):
        rowone = False
        colone = False
        size_rows = len(matrix)
        size_cols = len(matrix[0])
        for i in range(size_cols):
            if matrix[0][i] == 0:
                rowone = True
                break
        for i in range(size_rows):
            if matrix[i][0]==0:
                colone = True
                break
        for row in range(1, size_rows):
            for col in range(1, size_cols):
                if matrix[row][col]==0:
                    matrix[row][0] = 0
                    matrix[0][col] =0
        for i in range(1, size_rows):
            for j in range(1, size_cols):
                if matrix[i][0] ==0 or matrix[0][j] ==0:
                    matrix[i][j] =0
        if rowone==True:
            for i in range(size_cols):
                matrix[0][i] =0
        if colone==True:
            for i in range(size_rows):
                matrix[i][0] =0
        return matrix


a = Solution()
matrix = [[3,5,5,6,9,1,4,5,0,5],
          [2,7,9,5,9,5,4,9,6,8],
          [6,0,7,8,1,0,1,6,8,1],
          [7,2,6,5,8,5,6,5,0,6],
          [2,3,3,1,0,4,6,5,3,5],
          [5,9,7,3,8,8,5,1,4,3],
          [2,4,7,9,9,8,4,7,3,7],
          [3,5,2,8,8,2,2,4,9,8]]
a.setZeroes(matrix)