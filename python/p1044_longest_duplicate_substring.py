class Solution:
    def longestDupSubstring(self, s):
        size = len(s)
        if size < 2:
            return ''
        suffixes = list(range(size))
        ranks = [ord(char) for char in s]
        width = 1
        while width < size:
            def key(index):
                return ranks[index],ranks[index + width] if index + width < size else -1

            suffixes.sort(key=key)
            following = [0] * size
            for position in range(1,size):
                previous,current = suffixes[position - 1],suffixes[position]
                following[current] = following[previous] + (key(previous) != key(current))
            ranks = following
            if ranks[suffixes[-1]] == size - 1:
                break
            width *= 2
        inverse = [0] * size
        for position,index in enumerate(suffixes):
            inverse[index] = position
        common = best = best_start = 0
        for first in range(size):
            position = inverse[first]
            if position == 0:
                common = 0
                continue
            second = suffixes[position - 1]
            while first + common < size and second + common < size and s[first + common] == s[second + common]:
                common += 1
            if common > best:
                best,best_start = common,first
            if common:
                common -= 1
        return s[best_start:best_start + best]
