'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a
space-separated sequence of one or more dictionary words.

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
'''

# bfs solution 
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        que = deque()
        que.append(0)
        words = set(wordDict)
        visited = set()
        while que:
            start = que.pop()
            if start in visited:
                continue
            for end in range(start+1, len(s)+1):
                word = s[start:end]
                if word in words:
                    print(word, end)
                    que.appendleft(end)
                    if end == len(s):
                        return True
                    visited.add(start)
        return False

# recursve solution with memoization
class Solution:
    def wordBreak(self, s, wordDict):
        return self.util(s, wordDict, 0, {})

    def util(self, s, book, index, wordsused):
        print(s, index)
        if index== len(s):
            return True
        if index in wordsused:
            return wordsused[index]
        path = []
        result = False
        for i in range(index, len(s)):
            val = s[i]
            path.append(val)
            word = ''.join(path)
            print(word)
            if word in book:
               result = (result or self.util (s, book, i+1, wordsused))
        wordsused[index] = result
        return wordsused[index]

# below is a brute force approach, to speed this up we could memoize ofc
class Solution2:
    def wordBreak(self, s, wordDict):
        chars = list(s)
        return self.util(chars, wordDict, 0)

    def util(self, s, book, index):
        print(s, index)
        if index== len(s):
            return True
        path = []
        result = False
        for i in range(index, len(s)):
            val = s[i]
            path.append(val)
            word = ''.join(path)
            print(word)
            if word in book:
               result = self.util (s, book, i+1)
        return result

s = "abcd"

wordDict = ["a","abc","b","cd"]
# wordDict = ["apple", "pen"]
a = Solution()
print(a.wordBreak(s, wordDict))