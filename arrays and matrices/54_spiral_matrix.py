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

class Solution(object):
    def spiralOrder(self, matrix):
        output = {}
        return output.keys()

    def util(self, matrix, row, col, output, height, width ):

        return

matrix = [
[1, 2, 3, 4],
[10,11,12,5],
[9, 8, 7, 6]
]
m= [[1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]]
a = Solution()
print(a.spiralOrder(m))
# prints dict_keys([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# class Solution(object):
#     def spiralOrder(self, matrix):
#         output = {}
#         while len(output.keys()) < (len(matrix) * len(matrix[0])):
#             self.util(matrix, 0, 0, output, len(matrix)-1, len(matrix[0])-1)
#         return output.keys()
#
#     def util(self, matrix, row, col, output, height, width ):
#         if row > height or row < 0 or col > width or col < 0:
#             return
#         if matrix[row][col] not in output:
#             output[matrix[row][col]] = None
#             self.util(matrix, row, col+1, output, height, width )
#             self.util(matrix, row+1, col, output, height, width)
#             self.util(matrix, row, col - 1, output, height, width)
#             self.util(matrix, row-1, col, output, height, width)


            # print("test", row, col)