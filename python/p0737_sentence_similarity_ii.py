class Solution:
    def areSentencesSimilarTwo(self, sentence1, sentence2, similarPairs):
        if len(sentence1) != len(sentence2):
            return False
        parent, sizes = {}, {}

        def find(word):
            if word not in parent:
                parent[word], sizes[word] = word, 1
            while word != parent[word]:
                parent[word] = parent[parent[word]]
                word = parent[word]
            return word

        for left, right in similarPairs:
            first, second = find(left), find(right)
            if first != second:
                if sizes[first] < sizes[second]:
                    first, second = second, first
                parent[second] = first
                sizes[first] += sizes[second]
        return all(find(left) == find(right) for left, right in zip(sentence1, sentence2))
