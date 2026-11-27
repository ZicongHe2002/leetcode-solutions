from bisect import bisect_right


class Solution:
    def numSmallerByFrequency(self, queries, words):
        frequencies = sorted(word.count(min(word)) for word in words)
        return [len(words) - bisect_right(frequencies, query.count(min(query))) for query in queries]
