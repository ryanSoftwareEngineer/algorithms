'''
https://leetcode.com/problems/concatenated-words/
Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.

A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats";
"dogcatsdog" can be concatenated by "dog", "cats" and "dog";
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
'''

# This problem is similar to word break (not sure why this is a 'hard' problem when word break is 'medium')
# I chose the recursive solution for word break so here I chose the bfs solution
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordset = set(words)
        answers = []

        def helper(s):
            que = deque()
            for i in range(len(s)):
                word = s[0:i]
                if word in wordset and word != s:
                    que.append(i)
            while que:
                index = que.popleft()
                for i in range(index, len(s)):
                    word = s[index:i + 1]
                    if word in wordset and word != s:
                        if i + 1 == len(s):
                            answers.append(s)
                            return
                        que.append(i + 1)

        for word in words:
            helper(word)
        return answers