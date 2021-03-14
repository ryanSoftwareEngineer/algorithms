'''
Given a string s, return the longest palindromic substring in s.
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = [s[0]]
        if len(s) > 1:
            if s[1] == s[0]:
                ans.append(s[1])
        for i in range(2, len(s)):
            temp = []
            if s[i] == s[i - 2]:
                temp = self.get_palindrome(s, i - 2, i)
            if len(temp) > len(ans):
                ans = temp
            if s[i] == s[i - 1]:
                temp = self.get_palindrome(s, i - 1, i)
            if len(temp) > len(ans):
                ans = temp
        return ''.join(ans)

    def get_palindrome(self, s, a, b):
        while a > 0 and b < len(s) - 1 and s[a - 1] == s[b + 1]:
            a -= 1
            b += 1
        return list(s[a:b + 1])