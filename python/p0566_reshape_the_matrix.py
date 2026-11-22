class Solution:
    def matrixReshape(self, mat, r, c):
        rows, columns = len(mat), len(mat[0])
        if rows * columns != r * c:
            return mat
        output = [[0] * c for _ in range(r)]
        for index in range(rows * columns):
            output[index // c][index % c] = mat[index // columns][index % columns]
        return output
