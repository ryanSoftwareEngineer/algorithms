'''
https://leetcode.com/problems/basic-calculator-iii/
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, '+', '-', '*', '/' operators, and open '(' and closing parentheses ')'. The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Example 3:

Input: s = "2*(5+5*2)/3+(6/2+8)"
Output: 21
'''

#  one could approach this recursively ... anytime a '(' is encountered you run a new recursive function and return
# the inner expression

# another way is using two stacks (essentially same thing). There's also likely a BFS solution
# I went with the stacks solution here
class Solution:
    def calculate(self, s: str) -> int:
        nums = deque()
        ops = deque()
        current_number = 0

        def helpercalc(numa, numb, op):
            if op == '+':
                return numa + numb
            if op == '-':
                return numa - numb
            if op == '*':
                return numa * numb
            if op == '/':
                ans = abs(numa) // abs(numb)
                if numa < 0 != numb < 0:
                    ans *= -1
                return ans

        for ch in s:
            if ch.isnumeric():
                current_number *= 10
                current_number += int(ch)
            elif ch not in ['(', ')']:
                if ops and ops[-1] in ['*', '/']:
                    current_number = helpercalc(nums.pop(), current_number, ops.pop())
                nums.append(current_number)
                current_number = 0
                ops.append(ch)
            elif ch == '(':
                current_number = 0
                ops.append(ch)
            elif ch == ')':
                nums.append(current_number)
                while ops[-1] != '(':
                    valb = nums.pop()
                    vala = nums.pop()
                    op = ops.pop()
                    if ops and ops[-1] == '-':
                        vala *= -1
                        ops[-1] = '+'
                    val = helpercalc(vala, valb, op)
                    nums.append(val)
                ops.pop()
                current_number = nums.pop()
                if ops and ops[-1] in ['*', '/']:
                    current_number = helpercalc(nums.pop(), current_number, ops.pop())

        if ops and ops[-1] in ['*', '/']:
            current_number = helpercalc(nums.pop(), current_number, ops.pop())

        nums.append(current_number)
        while len(nums) > 1:
            valb = nums.pop()
            vala = nums.pop()
            op = ops.pop()
            if ops and ops[-1] == '-':
                vala *= -1
                ops[-1] = '+'
            val = helpercalc(vala, valb, op)
            nums.append(val)
        return nums.pop()

