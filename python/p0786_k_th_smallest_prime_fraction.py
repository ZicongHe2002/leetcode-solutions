class Solution:
    def kthSmallestPrimeFraction(self, arr, k):
        scale = 1 << 40
        size = len(arr)

        def count_and_best(bound):
            count, denominator = 0, 1
            best_num, best_den = 0, 1
            for numerator in range(size - 1):
                denominator = max(denominator, numerator + 1)
                while denominator < size and arr[numerator] * scale > bound * arr[denominator]:
                    denominator += 1
                if denominator == size:
                    break
                count += size - denominator
                if arr[numerator] * best_den > best_num * arr[denominator]:
                    best_num, best_den = arr[numerator], arr[denominator]
            return count, best_num, best_den

        low, high = 1, scale
        while low < high:
            middle = (low + high) // 2
            if count_and_best(middle)[0] >= k:
                high = middle
            else:
                low = middle + 1
        _, numerator, denominator = count_and_best(low)
        return [numerator, denominator]
