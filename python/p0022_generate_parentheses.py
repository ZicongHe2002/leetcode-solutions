class Solution:
    def generateParenthesis(self, n):
        result = []
        path = []

        def visit(opened, closed):
            if closed == n:
                result.append(''.join(path))
                return
            if opened < n:
                path.append('(')
                visit(opened + 1, closed)
                path.pop()
            if closed < opened:
                path.append(')')
                visit(opened, closed + 1)
                path.pop()

        visit(0, 0)
        return result
