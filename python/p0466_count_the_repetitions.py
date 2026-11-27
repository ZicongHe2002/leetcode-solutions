class Solution:
    def getMaxRepetitions(self, s1, n1, s2, n2):
        if n1 == 0 or set(s2) - set(s1):
            return 0
        index = matched = blocks = 0
        seen = {0: (0, 0)}
        while blocks < n1:
            for char in s1:
                if char == s2[index]:
                    index += 1
                    if index == len(s2):
                        matched += 1
                        index = 0
            blocks += 1
            if index in seen:
                previous_blocks, previous_matched = seen[index]
                cycle_blocks = blocks - previous_blocks
                cycle_matched = matched - previous_matched
                cycles = (n1 - blocks) // cycle_blocks
                blocks += cycles * cycle_blocks
                matched += cycles * cycle_matched
            else:
                seen[index] = (blocks, matched)
        return matched // n2
