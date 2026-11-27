from collections import deque


class StreamChecker:
    def __init__(self, words):
        self.trie = {}
        longest = 0
        for word in words:
            longest = max(longest,len(word))
            node = self.trie
            for char in reversed(word):
                node = node.setdefault(char,{})
            node['#'] = True
        self.history = deque(maxlen=longest)

    def query(self, letter):
        self.history.append(letter)
        node = self.trie
        for char in reversed(self.history):
            if char not in node:
                return False
            node = node[char]
            if '#' in node:
                return True
        return False
