class _TrieNode:
    def __init__(self):
        self.children = {}
        self.best = []


class AutocompleteSystem:
    def __init__(self, sentences, times):
        self._root = _TrieNode()
        self._counts = {}
        self._prefix = []
        self._node = self._root
        for sentence, count in zip(sentences, times):
            self._record(sentence, count)

    def _record(self, sentence, count):
        self._counts[sentence] = self._counts.get(sentence, 0) + count
        node = self._root
        for char in sentence:
            if char not in node.children:
                node.children[char] = _TrieNode()
            node = node.children[char]
            if sentence not in node.best:
                node.best.append(sentence)
            node.best.sort(key=lambda item: (-self._counts[item], item))
            del node.best[3:]

    def input(self, c):
        if c == '#':
            self._record(''.join(self._prefix), 1)
            self._prefix = []
            self._node = self._root
            return []
        self._prefix.append(c)
        if self._node is not None:
            self._node = self._node.children.get(c)
        return list(self._node.best) if self._node is not None else []
