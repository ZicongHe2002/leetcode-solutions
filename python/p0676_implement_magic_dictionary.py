class MagicDictionary:
    def __init__(self):
        self.by_length = {}

    def buildDict(self, dictionary):
        self.by_length = {}
        for word in dictionary:
            self.by_length.setdefault(len(word), []).append(word)

    def search(self, searchWord):
        for word in self.by_length.get(len(searchWord), ()):
            differences = 0
            for first, second in zip(word, searchWord):
                differences += first != second
                if differences > 1:
                    break
            if differences == 1:
                return True
        return False
