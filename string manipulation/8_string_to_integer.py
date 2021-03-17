'''
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer
(similar to C/C++'s atoi function).
'''

# while not alphanumeric  or + or - move
#     if + or - save it to answer
#     while s[index] is numeric append to list
#     join list with answer

class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s)<1:
            return 0
        index = 0
        ans = ""
        while index < len(s)-1 and s[index] == ' ':
            index+=1
        if s[index]== '-':
            ans = '-'
            index+=1
        elif s[index]== '+':
            index+=1        
        char_list = []
        while index < len(s) and s[index].isnumeric():
            char_list.append(s[index])
            index+=1
        if len(char_list)==0:
            return 0
        ans += ''.join(char_list)
        ans = int(ans)
        ans = max(ans, -2**31)
        ans = min(ans, (2**31 -1))
        return ans