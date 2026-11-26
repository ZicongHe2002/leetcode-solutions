class Solution:
    def replaceWords(self, dictionary, sentence):
        root = {}
        for word in dictionary:
            node = root
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node[''] = word

        def replace(word):
            node = root
            for char in word:
                if char not in node:
                    return word
                node = node[char]
                if '' in node:
                    return node['']
            return word

        return ' '.join(replace(word) for word in sentence.split(' '))
