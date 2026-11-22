class Solution:
    def countRangeSum(self, nums, lower, upper):
        prefix = [0]
        for value in nums:
            prefix.append(prefix[-1] + value)
        buffer = [0] * len(prefix)

        def count(start, stop):
            if stop - start <= 1:
                return 0
            middle = (start + stop) // 2
            total = count(start, middle) + count(middle, stop)
            low = high = middle
            for left in range(start, middle):
                while low < stop and prefix[low] - prefix[left] < lower:
                    low += 1
                while high < stop and prefix[high] - prefix[left] <= upper:
                    high += 1
                total += high - low

            left, right, output = start, middle, start
            while left < middle and right < stop:
                if prefix[left] <= prefix[right]:
                    buffer[output] = prefix[left]
                    left += 1
                else:
                    buffer[output] = prefix[right]
                    right += 1
                output += 1
            while left < middle:
                buffer[output] = prefix[left]
                left += 1
                output += 1
            while right < stop:
                buffer[output] = prefix[right]
                right += 1
                output += 1
            prefix[start:stop] = buffer[start:stop]
            return total

        return count(0, len(prefix))
