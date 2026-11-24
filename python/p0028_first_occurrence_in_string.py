class Solution:
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        borders = [0] * len(needle)
        matched = 0
        for index in range(1, len(needle)):
            while matched and needle[index] != needle[matched]:
                matched = borders[matched - 1]
            if needle[index] == needle[matched]:
                matched += 1
            borders[index] = matched
        matched = 0
        for index, character in enumerate(haystack):
            while matched and character != needle[matched]:
                matched = borders[matched - 1]
            if character == needle[matched]:
                matched += 1
            if matched == len(needle):
                return index - len(needle) + 1
        return -1
