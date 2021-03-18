
'''Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
Input: strs = ["flower","flow","flight"]
Output: "fl"
'''

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) < 1:
            return ""
        ans = []
        i = 0
        while i < len(strs[0]):
            for j in range(1, len(strs)):
                word = strs[j]
                if i >= len(word) or word[i] != strs[j - 1][i]:
                    return ''.join(ans)
            ans.append(strs[0][i])
            i += 1
        return ''.join(ans)
