from itertools import product
import unittest

from python.p0551_student_attendance_record_i import Solution


def streaming_day_state_oracle(record):
    absences = late_run = 0
    for day in record:
        if day == 'A':
            absences += 1
        late_run = late_run + 1 if day == 'L' else 0
        if absences >= 2 or late_run >= 3:
            return False
    return True


class AttendanceEligibilityTests(unittest.TestCase):
    def check(self, record, expected=None):
        actual = Solution().checkRecord(record)
        self.assertIs(type(actual), bool)
        self.assertEqual(actual, streaming_day_state_oracle(record) if expected is None else expected)

    def test_every_short_record_against_independent_daily_state(self):
        records = 0
        for size in range(1, 10):
            for days in product('ALP', repeat=size):
                self.check(''.join(days))
                records += 1
        self.assertEqual(records, 29523)

    def test_maximum_length_absence_totals_and_late_run_thresholds(self):
        self.check('P' * 1000, True)
        self.check('A' + 'P' * 999, True)
        self.check('A' + 'P' * 998 + 'A', False)
        self.check('LLP' * 333 + 'L', True)
        self.check('P' * 997 + 'LLL', False)
        self.check('L' * 1000, False)
        self.check('LLALL', True)
        self.check('LLPLL', True)
        self.check('PPALLP', True)
        self.check('PPALLL', False)


if __name__ == '__main__':
    unittest.main()
