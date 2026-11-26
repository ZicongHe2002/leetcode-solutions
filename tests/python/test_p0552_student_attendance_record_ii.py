from itertools import product
import unittest

from python.p0552_student_attendance_record_ii import Solution


MODULUS = 10**9 + 7


def exhaustive_record_filter(n):
    valid = 0
    for days in product('ALP', repeat=n):
        record = ''.join(days)
        valid += record.count('A') < 2 and 'LLL' not in record
    return valid


def unique_absence_position_oracle(n):
    without_absence = [1, 2, 4]
    while len(without_absence) <= n:
        without_absence.append(sum(without_absence[-3:]) % MODULUS)
    return (without_absence[n] + sum(without_absence[left] * without_absence[n - 1 - left]
                                    for left in range(n))) % MODULUS


class ConstantAttendanceStateTests(unittest.TestCase):
    def check(self, n, expected):
        actual = Solution().checkRecord(n)
        self.assertIs(type(actual), int)
        self.assertEqual(actual, expected)
        self.assertGreaterEqual(actual, 0)
        self.assertLess(actual, MODULUS)

    def test_every_small_length_against_literal_record_enumeration(self):
        for n in range(1, 10):
            self.check(n, exhaustive_record_filter(n))

    def test_large_lengths_against_independent_unique_absence_decomposition(self):
        for n in (10, 50, 1000, 10101, 99999, 100000):
            self.check(n, unique_absence_position_oracle(n))
        self.check(10101, 183236316)


if __name__ == '__main__':
    unittest.main()
