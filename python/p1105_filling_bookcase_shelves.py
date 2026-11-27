class Solution:
    def minHeightShelves(self, books, shelfWidth):
        count = len(books)
        best = [0] + [float('inf')] * count
        for end in range(1, count + 1):
            width = height = 0
            for start in range(end - 1, -1, -1):
                width += books[start][0]
                if width > shelfWidth:
                    break
                height = max(height, books[start][1])
                best[end] = min(best[end], best[start] + height)
        return best[count]
