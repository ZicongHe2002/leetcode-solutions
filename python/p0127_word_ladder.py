from collections import deque
from string import ascii_lowercase


class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        remaining = set(wordList)
        if endWord not in remaining:
            return 0
        remaining.discard(beginWord)
        queue = deque([(beginWord, 1)])
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for index, original in enumerate(word):
                for letter in ascii_lowercase:
                    if letter == original:
                        continue
                    following = word[:index] + letter + word[index + 1:]
                    if following in remaining:
                        remaining.remove(following)
                        queue.append((following, length + 1))
        return 0
