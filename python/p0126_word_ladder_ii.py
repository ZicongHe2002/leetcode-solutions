from collections import defaultdict
from string import ascii_lowercase


class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        if beginWord == endWord:
            return [[beginWord]]
        remaining = set(wordList)
        if endWord not in remaining:
            return []
        parents = defaultdict(set)
        frontier = {beginWord}
        while frontier and endWord not in frontier:
            remaining.difference_update(frontier)
            following = set()
            for word in frontier:
                for index in range(len(word)):
                    for letter in ascii_lowercase:
                        if letter == word[index]:
                            continue
                        candidate = word[:index] + letter + word[index + 1:]
                        if candidate in remaining:
                            parents[candidate].add(word)
                            following.add(candidate)
            frontier = following
        if endWord not in frontier:
            return []
        answers = []
        path = [endWord]

        def reconstruct(word):
            if word == beginWord:
                answers.append(path[::-1])
                return
            for previous in parents[word]:
                path.append(previous)
                reconstruct(previous)
                path.pop()

        reconstruct(endWord)
        return answers
