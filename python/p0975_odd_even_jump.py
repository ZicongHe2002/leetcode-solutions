class Solution:
    def oddEvenJumps(self, arr):
        size = len(arr)

        def successors(order):
            result = [-1] * size
            stack = []
            for index in order:
                while stack and stack[-1] < index:
                    result[stack.pop()] = index
                stack.append(index)
            return result

        higher = successors(sorted(range(size),key=lambda index:(arr[index],index)))
        lower = successors(sorted(range(size),key=lambda index:(-arr[index],index)))
        odd = [False] * size
        even = [False] * size
        odd[-1] = even[-1] = True
        for index in range(size - 2,-1,-1):
            if higher[index] >= 0:
                odd[index] = even[higher[index]]
            if lower[index] >= 0:
                even[index] = odd[lower[index]]
        return sum(odd)
