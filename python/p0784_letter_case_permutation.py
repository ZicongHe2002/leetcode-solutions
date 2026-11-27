class Solution:
    def letterCasePermutation(self, s):
        chars = list(s)
        result = []

        def visit(index):
            if index == len(s):
                result.append(''.join(chars))
                return
            if s[index].isalpha():
                chars[index] = s[index].lower()
                visit(index + 1)
                chars[index] = s[index].upper()
                visit(index + 1)
            else:
                visit(index + 1)

        visit(0)
        return result
