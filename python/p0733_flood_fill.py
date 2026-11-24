class Solution:
    def floodFill(self, image, sr, sc, color):
        original = image[sr][sc]
        if original == color:
            return image
        rows, columns = len(image), len(image[0])
        image[sr][sc] = color
        pending = [(sr, sc)]
        while pending:
            row, column = pending.pop()
            for nr, nc in ((row - 1, column), (row + 1, column),
                           (row, column - 1), (row, column + 1)):
                if 0 <= nr < rows and 0 <= nc < columns and image[nr][nc] == original:
                    image[nr][nc] = color
                    pending.append((nr, nc))
        return image
