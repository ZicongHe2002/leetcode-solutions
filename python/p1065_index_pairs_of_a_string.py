class Solution:
    def indexPairs(self, text, words):
        trie = {}
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char,{})
            node['#'] = True
        answer = []
        for start in range(len(text)):
            node = trie
            for end in range(start,len(text)):
                if text[end] not in node:
                    break
                node = node[text[end]]
                if '#' in node:
                    answer.append([start,end])
        return answer
