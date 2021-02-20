''' FIRST LEETCODE HARD!!!!!! LETS GO '''

'''Given an m x n board of characters and a list of strings words, return all words on the board.
Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are 
horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
'''

# add first letter of each word to hash table, add each word starting with that letter
# iterate through board if letter is in hash table do a bfs search for each word
# appending it to output if you do
class Solution:
    def findWords(self, board, words):
        book = {}
        output = set()
        for word in words:
            if word[0] not in book:
                book[word[0]]= [word]
            else:
                book[word[0]].append(word)
        for a in range(len(board)):
            for b in range(len(board[a])):
                  if board[a][b] in book:
                      start = board[a][b]
                      for c in book[start]:
                          if c not in output:
                            self.bfs(board, a, b, c, 0, [], output)
        # print(output)
        return output

    def bfs(self, board, row, col, word, index, path, output):
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[row]) or index > len(word):
            return
        if board[row][col] != word[index]:
            return
        if index >= len(word)-1:
            output.add(word)
            return
        # path.append(board[row][col])
        temp = board[row][col]
        board[row][col] = '#'
        self.bfs(board, row+1, col, word, index+1, path, output);
        self.bfs(board, row , col+1, word, index + 1, path, output);
        self.bfs(board, row - 1, col, word, index + 1, path, output);
        self.bfs(board, row , col-1, word, index + 1, path, output);
        board[row][col] = temp
        # path.pop()


board = [["a","b","c"],["a","e","d"],["a","f","g"]]
words = ["abcdefg","gfedcbaaa","eaabcdgfa","befa","dgc","ade"]
test = Solution()
test.findWords(board, words)