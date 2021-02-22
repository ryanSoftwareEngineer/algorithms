'''
Given an m x n board and a word, find if the word exists in the grid. The word can be constructed from letters of sequentially
adjacent cells, where "adjacent" cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
'''

class Solution:
    # iterate through array
    # if board[] value == word[0] run a dfs search
    def exist(self, board, word):
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == word[0]:
                    if self.util(board, row, col, set(), word, 0, []) == True:
                        return True
        return False

    def util(self, board, row, col, visited, word, index, path):
        if  row <0 or row >= len(board) or col <0 or col >= len(board[row]) or board[row][col] != word[index]  \
        or (row, col) in visited:
            return False
        path.append(board[row][col])
        print("path = ", path)
        if index+1 == len(word):
            return True
        visited.add((row,col))
        if self.util( board, row+1, col, visited, word, index+1, path) or self.util( board, row, col+1, visited, word, index+1, path) \
        or self.util(board, row-1, col, visited, word, index+1, path) or self.util( board, row, col-1, visited, word, index+1, path):
            return True
        visited.remove((row,col))
        path.pop()
        return False



board = [["A","B","C","E"],
         ["S","F","E","S"],
         ["A","D","E","E"]]
word = "ABCESEEEFS"
a = Solution()
print(a.exist(board, word))
# output:
# path =  ['A']
# path =  ['A', 'B']
# path =  ['A', 'B', 'C']
# path =  ['A', 'B', 'C', 'E']
# path =  ['A', 'B', 'C', 'E', 'S']
# path =  ['A', 'B', 'C', 'E', 'S', 'E']
# path =  ['A', 'B', 'C', 'E', 'S', 'E', 'E']
# path =  ['A', 'B', 'C', 'E', 'S', 'E']
# path =  ['A', 'B', 'C', 'E']
# path =  ['A', 'B', 'C', 'E', 'S']
# path =  ['A', 'B', 'C', 'E', 'S', 'E']
# path =  ['A', 'B', 'C', 'E', 'S', 'E', 'E']
# path =  ['A', 'B', 'C', 'E', 'S', 'E', 'E', 'E']
# path =  ['A', 'B', 'C', 'E', 'S', 'E', 'E', 'E', 'F']
# path =  ['A', 'B', 'C', 'E', 'S', 'E', 'E', 'E', 'F', 'S']
# True






