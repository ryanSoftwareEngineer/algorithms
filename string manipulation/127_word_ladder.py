'''


'''
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0

        que = deque()

        def combos(word):
            for a in range(len(word)):
                for b in range(26):
                    letter = chr(ord('a') + b)
                    # since string is immutable you should store this in char array before for b
                    # and ''.join(chararray[:a]+ letter  + chararray2[a+1:])
                    new = word[:a] + letter + word[a + 1:]
                    if new == beginWord:
                        return 1
                    if new in words:
                        que.append(new)
                        words.remove(new)
            return 0

        target = 0
        que.append(endWord)
        words.remove(endWord)
        while words or que:
            target += 1
            length = len(que)
            if length == 0:
                return 0
            for i in range(length):
                a = que.popleft()
                b = combos(a)
                if b:
                    return target + 1
        return 0