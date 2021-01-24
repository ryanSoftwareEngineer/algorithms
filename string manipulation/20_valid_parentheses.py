"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true
"""

# this solution is slightly slower than using a stack but it's a novel solution not on the solutions list
class Solution(object):
    def isValid(self, s):
        map = {"()", "{}", "[]"}
        one = 1
        while one < len(s):
            pair = s[one-1:one+1]
            if pair in map:
                s = s[0:one-1] + s[one+1:len(s)]
                one -=2
                continue
            one += 1
        return len(s)==0

a = Solution()
test_cases = ["([]{})", "[}[}"]
for test in test_cases:
    print(a.isValid(test))

"""
outputs:
one = 2 s = ([]{})
one = 1 s = ({})
one = 2 s = ({})
one = 1 s = ()
one = 0 s = 
True
one = 2 s = [}[}
one = 3 s = [}[}
one = 4 s = [}[}
False
"""