import heapq


class Solution:
    def smallestRange(self, nums):
        heap = [(values[0], row, 0) for row, values in enumerate(nums)]
        heapq.heapify(heap)
        right = max(value for value, _, _ in heap)
        best_left, best_right = heap[0][0], right
        while heap:
            left, row, index = heapq.heappop(heap)
            if (right - left, left) < (best_right - best_left, best_left):
                best_left, best_right = left, right
            if index + 1 == len(nums[row]):
                break
            successor = nums[row][index + 1]
            right = max(right, successor)
            heapq.heappush(heap, (successor, row, index + 1))
        return [best_left, best_right]
