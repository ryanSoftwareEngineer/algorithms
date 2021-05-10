'''
https://leetcode.com/problems/basic-calculator-ii/
Given a string s which represents an expression, evaluate this expression and return its value.

The integer division should truncate toward zero.

Input: s = "3+2*2"
Output: 7
'''
class Solution:
    def calculate(self, s: str) -> int:

        def multdiv(operand, que, cnum):
            if operand == '*':
                cnum *= que.pop()
            else:
                numer = que.pop()
                cnum = abs(numer )/ /cnum
                if numer <0:
                    cnum *= -1
            return cnum

        que = deque()
        cnum = 0
        operand = ''
        for num in s:
            if num == " ":
                continue
            if num.isnumeric():
                cnum *= 10
                cnum += int(num)
            elif operand == '*' or operand == '/':
                cnum = multdiv(operand, que, cnum)
                que.append(cnum)
                cnum = 0
                operand = num
            else:
                if operand == '-':
                    cnum *= -1
                que.append(cnum)
                operand = num
                cnum = 0

        if operand == '*' or operand == '/':
            cnum = multdiv(operand, que, cnum)
        if operand == '-':
            cnum *= -1
        while que:
            cnum += que.pop()
        return cnum
