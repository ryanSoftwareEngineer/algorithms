'''
Implement a trie with insert, search, and startsWith methods.
'''
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:

    def __init__(self):
        self.root = self.create_node()

    def create_node(self):
        return TrieNode()
    # def char_to_index(self, letter):
    #     # quesiton says "You may assume that all inputs are consist of lowercase letters a-z."
    #     return ord(letter) - ord('a')

    def insert(self, word: str) -> None:
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i]= self.create_node()
            node = node.children[i]
        node.end_of_word = True
        """
        Inserts a word into the trie.
        """

    def search(self, word: str) -> bool:
        node = self.root
        for i in word:
            if i not in node.children:
                return False
            node = node.children[i]
        return node.end_of_word
        """
        Returns if the word is in the trie.
        """

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for i in prefix:
            if i not in node.children:
                return False
            node = node.children[i]
        return True
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("apple")
param_2 = obj.search("apple")
print(param_2)
param_3 = obj.search("app")
print(param_3)
a4 = obj.startsWith("app")
print(a4)