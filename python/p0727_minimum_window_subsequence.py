class Solution:
    def minWindow(self, s1, s2):
        starts = [-1] * len(s2)
        best_start, best_length = 0, len(s1) + 1
        for end, char in enumerate(s1):
            for prefix in range(len(s2) - 1, -1, -1):
                if char == s2[prefix]:
                    if prefix == 0:
                        starts[0] = end
                    elif starts[prefix - 1] != -1:
                        starts[prefix] = starts[prefix - 1]
            if char == s2[-1] and starts[-1] != -1:
                length = end - starts[-1] + 1
                if length < best_length:
                    best_start, best_length = starts[-1], length
        return '' if best_length > len(s1) else s1[best_start:best_start + best_length]
