import unittest
from itertools import product
from statistics import median

from python.p0295_find_median_from_data_stream import MedianFinder


class MedianFinderTests(unittest.TestCase):
    def test_all_small_stream_prefixes_against_statistics_median(self):
        streams = checks = 0
        for size in range(1, 7):
            for values in product((-2, 0, 3), repeat=size):
                finder = MedianFinder()
                prefix = []
                streams += 1
                for value in values:
                    self.assertIsNone(finder.addNum(value))
                    prefix.append(value)
                    result = finder.findMedian()
                    self.assertIs(type(result), float)
                    self.assertEqual(result, median(prefix))
                    checks += 1
        self.assertEqual((streams, checks), (1092, 6015))

    def test_maximum_operation_counts_monotone_and_alternating_extreme_streams(self):
        increasing = MedianFinder()
        for index in range(25000):
            self.assertIsNone(increasing.addNum(-12500 + index))
            self.assertEqual(increasing.findMedian(), -12500 + index / 2)
        alternating = MedianFinder()
        for index in range(25000):
            self.assertIsNone(alternating.addNum(-100000 if index % 2 == 0 else 100000))
            self.assertEqual(alternating.findMedian(), -100000.0 if index % 2 == 0 else 0.0)
        single = MedianFinder()
        single.addNum(100000)
        self.assertEqual([single.findMedian() for _ in range(3)], [100000.0] * 3)


if __name__ == '__main__':
    unittest.main()
