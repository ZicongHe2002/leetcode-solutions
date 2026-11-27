from collections import Counter


class Solution:
    def findNumOfValidWords(self, words, puzzles):
        counts = Counter()
        for word in words:
            mask = 0
            for letter in word:
                mask |= 1 << (ord(letter) - ord('a'))
            if mask.bit_count() <= 7:
                counts[mask] += 1
        answer = []
        for puzzle in puzzles:
            first = 1 << (ord(puzzle[0]) - ord('a'))
            mask = 0
            for letter in puzzle:
                mask |= 1 << (ord(letter) - ord('a'))
            remaining = mask ^ first
            subset, total = remaining, 0
            while True:
                total += counts[subset | first]
                if subset == 0:
                    break
                subset = (subset - 1) & remaining
            answer.append(total)
        return answer
