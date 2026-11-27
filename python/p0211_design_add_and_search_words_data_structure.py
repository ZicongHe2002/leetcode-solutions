class WordDictionary:
    def __init__(self):
        self._root = {}

    def addWord(self, word):
        node = self._root
        for letter in word:
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node[None] = True

    def search(self, word):
        nodes = [self._root]
        for letter in word:
            if letter == '.':
                nodes = [child for node in nodes for key, child in node.items() if key is not None]
            else:
                nodes = [node[letter] for node in nodes if letter in node]
            if not nodes:
                return False
        return any(None in node for node in nodes)
