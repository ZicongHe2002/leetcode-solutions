class WordFilter:
    def __init__(self, words):
        self.latest = {}
        for index, word in enumerate(words):
            prefixes = [word[:end] for end in range(1, len(word) + 1)]
            suffixes = [word[start:] for start in range(len(word))]
            for prefix in prefixes:
                for suffix in suffixes:
                    self.latest[prefix, suffix] = index

    def f(self, pref, suff):
        return self.latest.get((pref, suff), -1)
