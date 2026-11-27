class Solution:
    def canThreePartsEqualSum(self, arr):
        total = sum(arr)
        if total % 3:
            return False
        target = total // 3
        current = parts = 0
        for index,value in enumerate(arr):
            current += value
            if current == target:
                parts += 1
                current = 0
                if parts == 2 and index < len(arr) - 1:
                    return True
        return False
