class Solution:
    def queryString(self, s, n):
        found = set()
        width = n.bit_length()
        for start,char in enumerate(s):
            if char == '0':
                continue
            value = 0
            for end in range(start,min(len(s),start + width)):
                value = (value << 1) | int(s[end])
                if value > n:
                    break
                found.add(value)
        return len(found) == n
