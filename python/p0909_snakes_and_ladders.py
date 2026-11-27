from collections import deque


class Solution:
    def snakesAndLadders(self, board):
        size = len(board)
        finish = size * size
        seen = {1}
        queue = deque([(1, 0)])
        while queue:
            position, moves = queue.popleft()
            for landing in range(position + 1, min(position + 6, finish) + 1):
                row_from_bottom, offset = divmod(landing - 1, size)
                column = offset if row_from_bottom % 2 == 0 else size - 1 - offset
                row = size - 1 - row_from_bottom
                following = board[row][column] if board[row][column] != -1 else landing
                if following == finish:
                    return moves + 1
                if following not in seen:
                    seen.add(following)
                    queue.append((following, moves + 1))
        return -1
