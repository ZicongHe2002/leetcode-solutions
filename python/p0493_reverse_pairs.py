class Solution:
    def reversePairs(self, nums):
        values = nums[:]
        buffer = [0] * len(values)

        def count(start, stop):
            if stop - start <= 1:
                return 0
            middle = (start + stop) // 2
            total = count(start, middle) + count(middle, stop)
            right = middle
            for left in range(start, middle):
                while right < stop and values[left] > 2 * values[right]:
                    right += 1
                total += right - middle

            left, right, output = start, middle, start
            while left < middle and right < stop:
                if values[left] <= values[right]:
                    buffer[output] = values[left]
                    left += 1
                else:
                    buffer[output] = values[right]
                    right += 1
                output += 1
            while left < middle:
                buffer[output] = values[left]
                left += 1
                output += 1
            while right < stop:
                buffer[output] = values[right]
                right += 1
                output += 1
            values[start:stop] = buffer[start:stop]
            return total

        return count(0, len(values))
