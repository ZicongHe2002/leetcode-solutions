class Solution:
    def duplicateZeros(self, arr):
        write = len(arr) + arr.count(0) - 1
        for read in range(len(arr) - 1, -1, -1):
            value = arr[read]
            if write < len(arr):
                arr[write] = value
            write -= 1
            if value == 0:
                if write < len(arr):
                    arr[write] = 0
                write -= 1
