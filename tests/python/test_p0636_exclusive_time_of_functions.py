import random
import unittest

from python.p0636_exclusive_time_of_functions import Solution


def generated_trace(rng):
    count = rng.randint(1, 5)
    logs, owners = [], []
    remaining = rng.randint(1, 25)

    def visit(identifier, depth):
        nonlocal remaining
        remaining -= 1
        logs.append(f'{identifier}:start:{len(owners)}')
        if depth < 5:
            for _ in range(rng.randrange(3)):
                owners.extend([identifier] * rng.randint(1, 3))
                if remaining:
                    visit(rng.randrange(count), depth + 1)
        owners.extend([identifier] * rng.randint(1, 3))
        logs.append(f'{identifier}:end:{len(owners) - 1}')

    for _ in range(rng.randint(1, 3)):
        if remaining:
            visit(rng.randrange(count), 0)
    expected = [owners.count(identifier) for identifier in range(count)]
    return count, logs, expected


class ExclusiveTimeTests(unittest.TestCase):
    def check(self, count, logs, expected):
        before = logs[:]
        result = Solution().exclusiveTime(count, logs)
        self.assertIs(type(result), list)
        self.assertTrue(all(type(value) is int for value in result))
        self.assertEqual(result, expected)
        self.assertEqual(logs, before)

    def test_thousand_generated_traces_against_direct_tick_owners(self):
        rng = random.Random(636)
        for _ in range(1000):
            count, logs, expected = generated_trace(rng)
            self.assertLessEqual(len(logs), 500)
            starts = [int(log.split(':')[2]) for log in logs if ':start:' in log]
            ends = [int(log.split(':')[2]) for log in logs if ':end:' in log]
            self.assertEqual(len(starts), len(set(starts)))
            self.assertEqual(len(ends), len(set(ends)))
            self.check(count, logs, expected)

    def test_inclusive_ends_recursion_idle_gaps_and_maximum_bounds(self):
        logs = [event for time in range(250)
                for event in (f'0:start:{time}', f'0:end:{time}')]
        self.check(100, logs, [250] + [0] * 99)
        self.check(100, ['99:start:0', '99:end:1000000000'], [0] * 99 + [1000000001])
        self.check(2, ['0:start:0', '0:end:0', '1:start:1000000000', '1:end:1000000000'], [1, 1])
        self.check(1, ['0:start:0', '0:start:2', '0:end:5', '0:start:6', '0:end:6', '0:end:7'], [8])
        self.check(2, ['0:start:0', '1:start:2', '1:end:5', '0:end:6'], [3, 4])


if __name__ == '__main__':
    unittest.main()
