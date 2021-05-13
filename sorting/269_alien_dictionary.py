'''
https://leetcode.com/problems/alien-dictionary/
There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted lexicographically by the rules of this new language.

Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.

A string s is lexicographically smaller than a string t if at the first letter where they differ, the letter in s comes before the letter in t in the alien language. If the first min(s.length, t.length) letters are the same, then s is smaller if and only if s.length < t.length.

Example
Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
'''

# here we create a graph of dependencies
# to find the topological sort i ran a dfs and put leaves on a stack 

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = defaultdict(list)
        letters = set()
        # create a set of all characters ... the question here is vague it says
        # the return value must use all characters as part of the question and some may not have dependencies
        for word in words:
            for ch in word:
                if ch not in letters:
                    letters.add(ch)


        # iterate through each word and compare to next word add any relationships that show lexigraphical order
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            a = 0
            if len(word2) < len(word1) and word2 == word1[0:len(word2)]:
                return ""
            while a < min(len(word1), len(word2)):
                if word1[a] != word2[a]:
                    graph[word1[a]].append(word2[a])
                    if word1[a] in letters:
                        letters.remove(word1[a])
                    if word2[a] in letters:
                        letters.remove(word2[a])
                    break
                a += 1
        leaves = set()
        visited = set()
        answer = []
        possible = True

        # i'm using a dfs to create a topologically sorted stack answers
        def helper(key):
            nonlocal answer
            nonlocal possible
            if possible == False:
                return
            visited.add(key)
            norepeat = set()
            for child in graph[key]:
                if child not in visited and child not in norepeat:
                    norepeat.add(child)
                    helper(child)
                elif child in visited and child not in leaves:
                    possible = False
                    return
            answer.append(key)
            leaves.add(key)

        # there may be multiple unconnected graphs so we need to dfs on all of them
        for word in words:
            for ch in word:
                if ch in graph and ch not in visited:
                    helper(ch)

        # any characters that don't belong to a graph are added in here you could have also called in the above loop
        # but the output is more coherent with seperation imo
        for ch in letters:
            answer.append(ch)

        # return the stack in reversed order
        return "".join(answer[::-1]) if possible else ""