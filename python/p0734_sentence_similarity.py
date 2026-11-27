class Solution:
    def areSentencesSimilar(self, sentence1, sentence2, similarPairs):
        if len(sentence1) != len(sentence2):
            return False
        pairs = {frozenset(pair) for pair in similarPairs}
        return all(left == right or frozenset((left, right)) in pairs
                   for left, right in zip(sentence1, sentence2))
