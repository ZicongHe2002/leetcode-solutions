from bisect import bisect_left


class Solution:
    def smallestCommonElement(self, mat):
        for value in mat[0]:
            present = True
            for row in mat[1:]:
                index = bisect_left(row, value)
                if index == len(row) or row[index] != value:
                    present = False
                    break
            if present:
                return value
        return -1
