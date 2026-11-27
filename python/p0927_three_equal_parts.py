class Solution:
    def threeEqualParts(self, arr):
        total = sum(arr)
        if total == 0:
            return [0,len(arr) - 1]
        if total % 3:
            return [-1,-1]
        per_part = total // 3
        starts = []
        seen = 0
        for index,bit in enumerate(arr):
            if bit:
                if seen in (0,per_part,2 * per_part):
                    starts.append(index)
                seen += 1
        length = len(arr) - starts[2]
        if starts[0] + length > starts[1] or starts[1] + length > starts[2]:
            return [-1,-1]
        for offset in range(length):
            if not arr[starts[0] + offset] == arr[starts[1] + offset] == arr[starts[2] + offset]:
                return [-1,-1]
        return [starts[0] + length - 1,starts[1] + length]
