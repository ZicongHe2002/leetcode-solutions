class Solution:
    def findWords(self, board, words):
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter, {})
            node['$'] = word
        rows, columns = len(board), len(board[0])
        result = []

        def visit(row, column, parent):
            letter = board[row][column]
            node = parent.get(letter)
            if node is None:
                return
            word = node.pop('$', None)
            if word is not None:
                result.append(word)
            board[row][column] = '#'
            for nr, nc in ((row - 1, column), (row + 1, column),
                           (row, column - 1), (row, column + 1)):
                if 0 <= nr < rows and 0 <= nc < columns and board[nr][nc] != '#':
                    visit(nr, nc, node)
            board[row][column] = letter
            if not node:
                del parent[letter]

        for row in range(rows):
            for column in range(columns):
                visit(row, column, trie)
        return result
