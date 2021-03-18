'''
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.
 For example, 121 is palindrome while -121 is not.
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        for left in range(0, len(x)):
            right = len(x)-left-1
            if left >= right:
                return True
            if x[left] != x[right]:
                return False