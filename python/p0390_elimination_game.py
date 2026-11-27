class Solution:
    def lastRemaining(self, n):
        head = step = 1
        remaining = n
        from_left = True
        while remaining > 1:
            if from_left or remaining % 2 == 1:
                head += step
            remaining //= 2
            step *= 2
            from_left = not from_left
        return head
