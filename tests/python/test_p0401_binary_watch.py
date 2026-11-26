from itertools import combinations
import unittest

from python.p0401_binary_watch import Solution


def led_subset_oracle(count):
    weights = (1, 2, 4, 8, 1, 2, 4, 8, 16, 32)
    result = set()
    for chosen in combinations(range(10), count):
        hour = sum(weights[index] for index in chosen if index < 4)
        minute = sum(weights[index] for index in chosen if index >= 4)
        if hour < 12 and minute < 60:
            result.add(str(hour) + ':' + str(minute).rjust(2, '0'))
    return result


class BinaryWatchValidTimeTests(unittest.TestCase):
    def test_entire_domain_against_led_combinations(self):
        for count in range(11):
            actual = Solution().readBinaryWatch(count)
            self.assertIs(type(actual), list)
            self.assertEqual(len(actual), len(set(actual)))
            self.assertEqual(set(actual), led_subset_oracle(count))
            for text in actual:
                hour, minute = text.split(':')
                self.assertEqual(hour, str(int(hour)))
                self.assertEqual(len(minute), 2)
                self.assertLess(int(hour), 12)
                self.assertLess(int(minute), 60)

    def test_zero_lights_valid_maximum_and_impossible_counts(self):
        self.assertEqual(Solution().readBinaryWatch(0), ['0:00'])
        self.assertEqual(len(Solution().readBinaryWatch(1)), 10)
        self.assertEqual(len(Solution().readBinaryWatch(8)), 8)
        self.assertEqual(Solution().readBinaryWatch(9), [])
        self.assertEqual(Solution().readBinaryWatch(10), [])


if __name__ == '__main__':
    unittest.main()
