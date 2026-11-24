class Solution:
    def partition(self, s):
        size = len(s)
        palindrome = [[False] * size for _ in range(size)]
        for start in range(size - 1, -1, -1):
            for end in range(start, size):
                palindrome[start][end] = (s[start] == s[end]
                                          and (end - start < 2 or palindrome[start + 1][end - 1]))
        result = []
        path = []

        def visit(start):
            if start == size:
                result.append(path[:])
                return
            for end in range(start, size):
                if palindrome[start][end]:
                    path.append(s[start:end + 1])
                    visit(end + 1)
                    path.pop()

        visit(0)
        return result
