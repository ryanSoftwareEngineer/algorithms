'''
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.
'''
class Solution(object):
    def rotate(self, matrix):
        a = 0
        b = len(matrix)-1
        while a < b:
            for i in range(a, b):
                temp = matrix[a][i]
                matrix[a][i] = matrix[b-(i-a)][a]
                matrix[b-(i-a)][a] = matrix[b][b-(i-a)]
                matrix[b][b-(i-a)] = matrix[i][b]
                matrix[i][b] = temp
            a+=1
            b-=1
        return matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
a = Solution()
a.rotate(matrix)
