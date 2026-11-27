class Solution:
    def shortestToChar(self, s, c):
        size = len(s)
        distances = [size] * size
        previous = -size
        for index,char in enumerate(s):
            if char == c:
                previous = index
            distances[index] = index - previous
        following = 2 * size
        for index in range(size - 1,-1,-1):
            if s[index] == c:
                following = index
            distances[index] = min(distances[index],following - index)
        return distances
