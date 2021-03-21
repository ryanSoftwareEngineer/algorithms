'''

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
'''
# 2nd
class Solution:
    def generateParenthesis(self, n: int):
        left = n
        right = 0
        answer = []
        self.helper(left, right, [], answer)
        return answer

    def helper(self, left, right, temparray, answer):
        if not left and not right:
            answer.append(''.join(temparray))
        if left:
            temparray.append('(')
            self.helper(left - 1, right + 1, temparray, answer)
            temparray.pop()
        if right:
            temparray.append(')')
            self.helper(left, right - 1, temparray, answer)
            temparray.pop()
# first attempt
class Solution2:
    def generateParenthesis(self, n: int):
        book = {}
        book['('] = n - 1
        book[')'] = n
        output = []
        temp = ['(']
        self.recur(book, temp, output)
        return output

    def recur(self, book, path, output):
        if book['('] == 0 and book[')'] == 0:
            output.append(''.join(path))
            return
        if book['('] > 0:
            path.append('(')
            book['('] -= 1
            self.recur(book, path, output)
            path.pop()
            book['('] += 1
        if book[')'] > 0 and book[')'] > book['(']:
            path.append(')')
            book[')'] -= 1
            self.recur(book, path, output)
            path.pop()
            book[')'] += 1