from functools import cache
from itertools import product


class Solution:
    def pyramidTransition(self, bottom, allowed):
        tops = {}
        for left, right, upper in allowed:
            tops.setdefault(left + right, []).append(upper)

        @cache
        def build(row):
            if len(row) == 1:
                return True
            choices = [tops.get(row[index:index + 2], ()) for index in range(len(row) - 1)]
            return any(build(''.join(upper)) for upper in product(*choices))

        return build(bottom)
