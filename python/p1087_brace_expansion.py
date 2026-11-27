class Solution:
    def expand(self, s):
        words = ['']
        index = 0
        while index < len(s):
            if s[index] == '{':
                end = s.index('}', index)
                choices = s[index + 1:end].split(',')
                index = end + 1
            else:
                choices = [s[index]]
                index += 1
            words = [prefix + choice for prefix in words for choice in choices]
        return sorted(words)
