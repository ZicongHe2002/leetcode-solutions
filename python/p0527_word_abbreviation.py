class Solution:
    def wordsAbbreviation(self, words):
        groups = {}
        for index, word in enumerate(words):
            groups.setdefault((len(word), word[0], word[-1]), []).append((word, index))
        answer = list(words)
        for entries in groups.values():
            entries.sort()
            prefixes = [1] * len(entries)
            for index in range(1, len(entries)):
                left, right = entries[index - 1][0], entries[index][0]
                common = 0
                while common < len(left) and left[common] == right[common]:
                    common += 1
                needed = common + 1
                prefixes[index - 1] = max(prefixes[index - 1], needed)
                prefixes[index] = max(prefixes[index], needed)
            for (word, original_index), prefix in zip(entries, prefixes):
                removed = len(word) - prefix - 1
                if removed > 1:
                    answer[original_index] = word[:prefix] + str(removed) + word[-1]
        return answer
