import unittest
from itertools import combinations, product

from python.p0715_range_module import RangeModule


class RangeModuleTests(unittest.TestCase):
    def test_all_short_api_programs_against_real_unit_cell_coverage(self):
        intervals = ((1, 2), (2, 3), (1, 3), (3, 4))
        choices = [(action, left, right) for action in ('addRange', 'removeRange', 'queryRange')
                   for left, right in intervals]
        queries = tuple(combinations(range(1, 6), 2))
        checked = 0
        for size in range(1, 5):
            for program in product(choices, repeat=size):
                obj, cells = RangeModule(), set()
                for action, left, right in program:
                    result = getattr(obj, action)(left, right)
                    if action == 'addRange':
                        cells.update(range(left, right))
                        self.assertIsNone(result)
                    elif action == 'removeRange':
                        cells.difference_update(range(left, right))
                        self.assertIsNone(result)
                    else:
                        self.assertIs(type(result), bool)
                        self.assertEqual(result, all(cell in cells for cell in range(left, right)))
                    for qleft, qright in queries:
                        result = obj.queryRange(qleft, qright)
                        self.assertIs(type(result), bool)
                        self.assertEqual(result, all(cell in cells for cell in range(qleft, qright)))
                checked += 1
        self.assertEqual(checked, 22620)

    def test_ten_thousand_calls_billion_endpoints_touching_and_middle_removal(self):
        obj = RangeModule()
        calls = 0
        for i in range(5000):
            obj.addRange(2 * i + 1, 2 * i + 2)
            calls += 1
        for i in range(5000):
            self.assertEqual(obj.queryRange(2 * i + 1, 2 * i + 2), True)
            calls += 1
        self.assertEqual(calls, 10000)
        other = RangeModule()
        other.addRange(1, 10**9)
        other.removeRange(10**9 - 2, 10**9 - 1)
        self.assertTrue(other.queryRange(1, 10**9 - 2))
        self.assertFalse(other.queryRange(10**9 - 3, 10**9 - 1))
        self.assertTrue(other.queryRange(10**9 - 1, 10**9))
        other.addRange(10**9 - 2, 10**9 - 1)
        self.assertTrue(other.queryRange(1, 10**9))
        other.removeRange(1, 10**9)
        self.assertFalse(other.queryRange(1, 2))
        other.removeRange(2, 3)
        other.addRange(10, 14)
        other.addRange(14, 20)
        self.assertTrue(other.queryRange(10, 20))
        other.removeRange(14, 16)
        self.assertTrue(other.queryRange(10, 14))
        self.assertFalse(other.queryRange(13, 15))
        self.assertTrue(other.queryRange(16, 17))


if __name__ == '__main__':
    unittest.main()
