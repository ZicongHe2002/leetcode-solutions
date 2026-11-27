from functools import lru_cache


class Solution:
    def removeBoxes(self, boxes):
        @lru_cache(None)
        def best(left, right, carried):
            if left > right:
                return 0
            while left < right and boxes[right - 1] == boxes[right]:
                right -= 1
                carried += 1
            answer = best(left, right - 1, 0) + (carried + 1) ** 2
            for middle in range(left, right):
                if boxes[middle] == boxes[right]:
                    answer = max(answer, best(left, middle, carried + 1) +
                                 best(middle + 1, right - 1, 0))
            return answer

        return best(0, len(boxes) - 1, 0)
