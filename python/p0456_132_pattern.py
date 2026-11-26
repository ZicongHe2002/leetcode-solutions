class Solution:
    def find132pattern(self, nums):
        descending = []
        middle = None
        for value in reversed(nums):
            if middle is not None and value < middle:
                return True
            while descending and value > descending[-1]:
                popped = descending.pop()
                if middle is None or popped > middle:
                    middle = popped
            descending.append(value)
        return False
