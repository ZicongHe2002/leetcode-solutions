class Solution:
    def prevPermOpt1(self, arr):
        result = arr[:]
        pivot = len(result) - 2
        while pivot >= 0 and result[pivot] <= result[pivot + 1]:
            pivot -= 1
        if pivot < 0:
            return result
        partner = len(result) - 1
        while result[partner] >= result[pivot]:
            partner -= 1
        while partner > pivot + 1 and result[partner] == result[partner - 1]:
            partner -= 1
        result[pivot],result[partner] = result[partner],result[pivot]
        return result
