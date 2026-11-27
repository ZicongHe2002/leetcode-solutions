from functools import lru_cache
from itertools import product
import unittest

from python.p0455_assign_cookies import Solution


def all_assignments(needs, cookies):
    @lru_cache(None)
    def assign(child, used):
        if child == len(needs):
            return 0
        best = assign(child + 1, used)
        for index, cookie in enumerate(cookies):
            if not (used >> index & 1) and cookie >= needs[child]:
                best = max(best, 1 + assign(child + 1, used | (1 << index)))
        return best
    return assign(0, 0)


class CookieMatchingTests(unittest.TestCase):
    def check(self, needs, cookies, expected=None):
        before = (needs[:], cookies[:])
        if expected is None:
            expected = all_assignments(needs, cookies)
        result = Solution().findContentChildren(needs, cookies)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual((needs, cookies), before)

    def test_all_small_children_and_cookie_arrays_against_matching_search(self):
        needs_cases = [list(values) for size in range(1, 5) for values in product((1, 2, 3), repeat=size)]
        cookie_cases = [list(values) for size in range(5) for values in product((1, 2, 3), repeat=size)]
        checks = 0
        for needs in needs_cases:
            for cookies in cookie_cases:
                self.check(needs, cookies)
                checks += 1
        self.assertEqual(checks, 14520)

    def test_maximum_lengths_empty_cookies_and_integer_limit(self):
        self.check([2147483647] * 30000, [2147483647] * 30000, 30000)
        self.check([2147483647] * 30000, [1] * 30000, 0)
        self.check([1] * 30000, [], 0)
        self.check(list(range(30000, 0, -1)), list(range(1, 30001)), 30000)


if __name__ == '__main__':
    unittest.main()
