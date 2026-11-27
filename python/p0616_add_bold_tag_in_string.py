class Solution:
    def addBoldTag(self, s, words):
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter, {})
            node[None] = True
        delta = [0] * (len(s) + 1)
        for start in range(len(s)):
            node = trie
            end = longest = start
            while end < len(s) and s[end] in node:
                node = node[s[end]]
                end += 1
                if None in node:
                    longest = end
            if longest > start:
                delta[start] += 1
                delta[longest] -= 1
        pieces = []
        active = 0
        bold = False
        for index, letter in enumerate(s):
            active += delta[index]
            covered = active > 0
            if covered and not bold:
                pieces.append('<b>')
            elif bold and not covered:
                pieces.append('</b>')
            pieces.append(letter)
            bold = covered
        if bold:
            pieces.append('</b>')
        return ''.join(pieces)
