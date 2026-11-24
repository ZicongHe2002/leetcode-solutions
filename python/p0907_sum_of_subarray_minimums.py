class Solution:
    def sumSubarrayMins(self, arr):
        modulus = 10**9 + 7
        pending = []
        total = 0
        for right in range(len(arr) + 1):
            current = arr[right] if right < len(arr) else 0
            while pending and arr[pending[-1]] >= current:
                index = pending.pop()
                left = pending[-1] if pending else -1
                total = (total + arr[index] * (index - left) * (right - index)) % modulus
            if right < len(arr):
                pending.append(right)
        return total
