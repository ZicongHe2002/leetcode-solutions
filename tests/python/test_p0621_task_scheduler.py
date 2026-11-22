import unittest
from functools import lru_cache
from itertools import product
from string import ascii_uppercase

from python.p0621_task_scheduler import Solution


@lru_cache(None)
def shortest_schedule_by_states(remaining, waiting, cooldown):
    if not any(remaining):
        return 0
    available = [i for i, count in enumerate(remaining) if count and waiting[i] == 0]
    if not available:
        jump = min(waiting[i] for i, count in enumerate(remaining) if count)
        after_wait = tuple(max(0, value - jump) for value in waiting)
        return jump + shortest_schedule_by_states(remaining, after_wait, cooldown)
    lengths = []
    for task in available:
        after_task = list(remaining)
        after_task[task] -= 1
        after_wait = [max(0, value - 1) for value in waiting]
        after_wait[task] = cooldown
        lengths.append(1 + shortest_schedule_by_states(tuple(after_task), tuple(after_wait), cooldown))
    return min(lengths)


class TaskSchedulerTests(unittest.TestCase):
    def check(self, tasks, cooldown, expected=None):
        before = tasks[:]
        if expected is None:
            remaining = tuple(tasks.count(letter) for letter in 'ABC')
            expected = shortest_schedule_by_states(remaining, (0, 0, 0), cooldown)
        result = Solution().leastInterval(tasks, cooldown)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(tasks, before)

    def test_all_small_three_task_multisets_against_cooldown_state_search(self):
        cases = checks = 0
        for counts in product(range(4), repeat=3):
            if not any(counts):
                continue
            tasks = [letter for letter, count in zip('ABC', counts) for _ in range(count)]
            cases += 1
            for cooldown in range(4):
                self.check(list(reversed(tasks)), cooldown)
                checks += 1
        self.assertEqual((cases, checks), (63, 252))

    def test_maximum_task_count_cooldown_tied_frequencies_and_empty_extension(self):
        self.check(['A'] * 10000, 100, 1009900)
        self.check(['A'] * 10000, 0, 10000)
        mixed = list(ascii_uppercase) * 384 + list(ascii_uppercase[:16])
        self.assertEqual(len(mixed), 10000)
        self.check(mixed, 25, 10000)
        self.check(mixed, 100, 38800)
        self.check(list('AAABBB'), 2, 8)
        self.check([], 100, 0)


if __name__ == '__main__':
    unittest.main()
