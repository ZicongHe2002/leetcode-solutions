class Solution:
    def palindromePairs(self, words):
        indices = {word: index for index, word in enumerate(words)}
        answers = set()
        for index, word in enumerate(words):
            for cut in range(len(word) + 1):
                prefix, suffix = word[:cut], word[cut:]
                if prefix == prefix[::-1]:
                    previous = indices.get(suffix[::-1])
                    if previous is not None and previous != index:
                        answers.add((previous, index))
                if cut < len(word) and suffix == suffix[::-1]:
                    following = indices.get(prefix[::-1])
                    if following is not None and following != index:
                        answers.add((index, following))
        return [list(pair) for pair in answers]
