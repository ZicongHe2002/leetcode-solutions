class Solution:
    def strangePrinter(self, s):
        characters = []
        for char in s:
            if not characters or characters[-1] != char:
                characters.append(char)
        size = len(characters)
        best = [[0] * size for _ in range(size)]
        for left in range(size - 1, -1, -1):
            best[left][left] = 1
            for right in range(left + 1, size):
                best[left][right] = 1 + best[left + 1][right]
                for match in range(left + 1, right + 1):
                    if characters[match] == characters[left]:
                        middle = best[left + 1][match - 1] if match > left + 1 else 0
                        best[left][right] = min(best[left][right], middle + best[match][right])
        return best[0][-1]
