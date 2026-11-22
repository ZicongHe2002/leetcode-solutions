class Trie:
    def __init__(self):
        self._root = {}

    def insert(self, word):
        node = self._root
        for letter in word:
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node[None] = True

    def _find(self, text):
        node = self._root
        for letter in text:
            if letter not in node:
                return None
            node = node[letter]
        return node

    def search(self, word):
        node = self._find(word)
        return node is not None and None in node

    def startsWith(self, prefix):
        return self._find(prefix) is not None
