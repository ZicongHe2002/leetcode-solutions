from array import array


def _palindromic_edges(word):
    length = len(word)
    prefixes = bytearray(length + 1)
    suffixes = bytearray(length + 1)
    prefixes[0] = suffixes[length] = 1

    odd = [0] * length
    left, right = 0, -1
    for center in range(length):
        radius = 1 if center > right else min(odd[left + right - center], right - center + 1)
        while center - radius >= 0 and center + radius < length and word[center - radius] == word[center + radius]:
            radius += 1
        odd[center] = radius
        if center - radius + 1 == 0:
            prefixes[center + radius] = 1
        if center + radius == length:
            suffixes[center - radius + 1] = 1
        if center + radius - 1 > right:
            left, right = center - radius + 1, center + radius - 1

    even = [0] * length
    left, right = 0, -1
    for center in range(length):
        radius = 0 if center > right else min(even[left + right - center + 1], right - center + 1)
        while center - radius - 1 >= 0 and center + radius < length and word[center - radius - 1] == word[center + radius]:
            radius += 1
        even[center] = radius
        if center - radius == 0:
            prefixes[center + radius] = 1
        if center + radius == length:
            suffixes[center - radius] = 1
        if center + radius - 1 > right:
            left, right = center - radius, center + radius - 1

    return prefixes, suffixes


class _ReverseTrie:
    def __init__(self):
        self.first_child = array('i', [-1])
        self.next_sibling = array('i', [-1])
        self.letter = array('B', [0])
        self.terminal = array('i', [-1])
        self.palindrome_head = array('i', [-1])
        self.palindrome_word = array('i')
        self.next_palindrome = array('i')

    def follow(self, node, letter):
        child = self.first_child[node]
        while child != -1:
            if self.letter[child] == letter:
                return child
            child = self.next_sibling[child]
        return -1

    def extend(self, node, letter):
        child = self.follow(node, letter)
        if child != -1:
            return child
        child = len(self.first_child)
        self.first_child.append(-1)
        self.next_sibling.append(self.first_child[node])
        self.letter.append(letter)
        self.terminal.append(-1)
        self.palindrome_head.append(-1)
        self.first_child[node] = child
        return child

    def add_palindrome(self, node, word_index):
        entry = len(self.palindrome_word)
        self.palindrome_word.append(word_index)
        self.next_palindrome.append(self.palindrome_head[node])
        self.palindrome_head[node] = entry


class Solution:
    def palindromePairs(self, words):
        trie = _ReverseTrie()
        suffix_flags = []
        for index, word in enumerate(words):
            prefixes, suffixes = _palindromic_edges(word)
            suffix_flags.append(suffixes)
            node = 0
            for position in range(len(word) - 1, -1, -1):
                if prefixes[position + 1]:
                    trie.add_palindrome(node, index)
                node = trie.extend(node, ord(word[position]) - ord('a'))
            trie.terminal[node] = index
            trie.add_palindrome(node, index)

        answers = []
        for index, word in enumerate(words):
            node = 0
            for position, letter in enumerate(word):
                partner = trie.terminal[node]
                if partner != -1 and partner != index and suffix_flags[index][position]:
                    answers.append([index, partner])
                node = trie.follow(node, ord(letter) - ord('a'))
                if node == -1:
                    break
            else:
                entry = trie.palindrome_head[node]
                while entry != -1:
                    partner = trie.palindrome_word[entry]
                    if partner != index:
                        answers.append([index, partner])
                    entry = trie.next_palindrome[entry]
        return answers
