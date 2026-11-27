class Solution:
    def lengthLongestPath(self, input):
        prefixes = [0]
        best = index = 0
        while index < len(input):
            depth = 0
            while index < len(input) and input[index] == '\t':
                depth += 1
                index += 1
            start = index
            is_file = False
            while index < len(input) and input[index] != '\n':
                if input[index] == '.':
                    is_file = True
                index += 1
            length = index - start
            if is_file:
                best = max(best, prefixes[depth] + length)
            else:
                next_prefix = prefixes[depth] + length + 1
                if depth + 1 == len(prefixes):
                    prefixes.append(next_prefix)
                else:
                    prefixes[depth + 1] = next_prefix
            index += 1
        return best
