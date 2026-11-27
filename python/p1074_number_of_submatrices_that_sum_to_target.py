class Solution:
    def numSubmatrixSumTarget(self, matrix, target):
        rows,columns = len(matrix),len(matrix[0])
        answer = 0
        for top in range(rows):
            totals = [0] * columns
            for bottom in range(top,rows):
                for column in range(columns):
                    totals[column] += matrix[bottom][column]
                frequency = {0:1}
                prefix = 0
                for value in totals:
                    prefix += value
                    answer += frequency.get(prefix - target,0)
                    frequency[prefix] = frequency.get(prefix,0) + 1
        return answer
