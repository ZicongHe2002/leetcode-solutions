import unittest
from itertools import product

from python.p0760_find_anagram_mappings import Solution


class AnagramMappingTests(unittest.TestCase):
    def check(self, nums1, nums2):
        before1, before2 = nums1[:], nums2[:]
        result = Solution().anagramMappings(nums1, nums2)
        self.assertIs(type(result), list)
        self.assertEqual(len(result), len(nums1))
        self.assertTrue(all(type(index) is int for index in result))
        self.assertEqual(sorted(result), list(range(len(nums2))))
        self.assertEqual([nums2[index] for index in result], nums1)
        self.assertEqual((nums1, nums2), (before1, before2))

    def test_all_small_equal_multiset_array_pairs_against_literal_bijection_contract(self):
        checked = 0
        for size in range(1, 7):
            groups = {}
            for values in product(range(3), repeat=size):
                groups.setdefault(tuple(sorted(values)), []).append(values)
            for group in groups.values():
                for nums1 in group:
                    for nums2 in group:
                        self.check(list(nums1), list(nums2))
                        checked += 1
        self.assertEqual(checked, 40572)

    def test_official_example_maximum_length_repeated_values_and_value_limit(self):
        self.check([12,28,46,32,50], [50,12,32,46,28])
        self.check([5] * 100, [5] * 100)
        self.check(list(range(100)), list(reversed(range(100))))
        self.check([0,10**5] * 50, [10**5] * 50 + [0] * 50)
        self.check([10**5], [10**5])


if __name__ == '__main__':
    unittest.main()
