''''Design a data structure that supports adding new words and finding if a string matches any previously added string.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word
 may contain dots '.' where dots can be matched with any letter.
'''

# i just built a regular trie and if a "." was encountered ran a dfs on all combinations
class Node:
    def __init__(self):
        self.children = [None for i in range(26)]
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = self.create_node()

    def create_node(self):
        return Node()

    def char_to_index(self, ch):
        return (ord(ch) - ord('a'))

    def addWord(self, word: str) -> None:
        node = self.root
        for i in word:
            index = self.char_to_index(i)
            if node.children[index] is None:
                node.children[index] = self.create_node()
            node = node.children[index]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for a, i in enumerate(word):
            if i == ".":
                return self.dfs(node, word, a)
            index = self.char_to_index(i)
            if not node.children[index]:
                print(node.children[index])
                return False
            node = node.children[index]
        return node.is_end== True

    def dfs(self, node, word, index):
        if index >= len(word):
            if node.is_end == True:
                return True
            else: return False
        ans = False
        for i, ref in enumerate(node.children):
            if (word[index] == '.' or self.char_to_index(word[index]) == i) and node.children[i]:
                ans = ans or self.dfs(ref, word, index+1)
        return ans


wordDictionary = WordDictionary();
wordDictionary.addWord("at");
wordDictionary.addWord("and");
wordDictionary.addWord("add");
# a= wordDictionary.search("pad");
# print(a)
# a= wordDictionary.search("bad");
# print(a)
# a= wordDictionary.search(".ad");
# print(a)
a= wordDictionary.search("a");
print(a)