'''
Given an m x n matrix, return all elements of the matrix in spiral order.
Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
'''

# iterate the matrix right until out of bounds
#  if position > len(matrix) or > len(matrix[0]) or <0 or in cache
# todo: instead of caching coordinates visited perhaps you could keep track of 4 numers a,b,c,d
#       for when to stop... when direction changes incremenent/decrement abcd as it should
# return ..
class Solution:
    def spiralOrder(self, matrix):
        output = {}
        self.util(matrix, 0, 0, output, len(matrix) - 1, len(matrix[0]) - 1)
        return output.values()

    def util(self, matrix, row, col, output, height, width):
        if row > height or row < 0 or col > width or col < 0 or (row, col) in output:
            return
        output[(row, col)] = matrix[row][col]
        if col == 0 or (row, col-1) in output:
            self.util(matrix, row - 1, col, output, height, width)
        self.util(matrix, row, col + 1, output, height, width)
        self.util(matrix, row + 1, col, output, height, width)
        self.util(matrix, row, col - 1, output, height, width)
        return


m= [
[1,2,3,4,5],
[2,1,0,1,6],
[3,6,7,2,7],
[4,5,4,3,8],
[5,6,7,8,9],
]
a = Solution()
print(a.spiralOrder(m))
# prints dict_values([1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7])
