class Solution:
    def repeatedStringMatch(self, a, b):
        prefix = [0] * len(b)
        matched = 0
        for index in range(1, len(b)):
            while matched and b[matched] != b[index]:
                matched = prefix[matched - 1]
            if b[matched] == b[index]:
                matched += 1
            prefix[index] = matched
        matched = 0
        for index in range(len(a) + len(b) - 1):
            char = a[index % len(a)]
            while matched and b[matched] != char:
                matched = prefix[matched - 1]
            if b[matched] == char:
                matched += 1
            if matched == len(b):
                return (index + len(a)) // len(a)
        return -1
