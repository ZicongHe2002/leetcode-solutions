class Solution:
    def countAndSay(self, n):
        term = '1'
        for _ in range(n - 1):
            pieces, start = [], 0
            for end in range(1, len(term) + 1):
                if end == len(term) or term[end] != term[start]:
                    pieces.extend((str(end - start), term[start]))
                    start = end
            term = ''.join(pieces)
        return term
