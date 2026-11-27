import unittest

from python.p0682_baseball_game import Solution


def historical_records(operations):
    history, active = {}, set()
    for index, operation in enumerate(operations):
        ordered = sorted(active)
        if operation == 'C':
            active.remove(ordered[-1])
            continue
        if operation == 'D':
            value = 2 * history[ordered[-1]]
        elif operation == '+':
            value = history[ordered[-1]] + history[ordered[-2]]
        else:
            value = int(operation)
        history[index] = value
        active.add(index)
    return sum(history[index] for index in active)


def legal_programs(prefix=(), scores=(), maximum=6):
    if prefix:
        yield prefix
    if len(prefix) == maximum:
        return
    choices = [(str(value), scores + (value,)) for value in (-2, 0, 3)]
    if scores:
        choices.extend((('C', scores[:-1]), ('D', scores + (2 * scores[-1],))))
    if len(scores) >= 2:
        choices.append(('+', scores + (scores[-2] + scores[-1],)))
    for operation, updated in choices:
        yield from legal_programs(prefix + (operation,), updated, maximum)


class BaseballGameTests(unittest.TestCase):
    def check(self, operations, expected=None):
        before = operations[:]
        result = Solution().calPoints(operations)
        self.assertIs(type(result), int)
        self.assertEqual(result, historical_records(operations) if expected is None else expected)
        self.assertEqual(operations, before)

    def test_every_short_legal_program_against_indexed_historical_records(self):
        for operations in legal_programs():
            self.check(list(operations))

    def test_thousand_operations_negative_scores_cancellations_and_int32_bounds(self):
        self.check(['30000'] * 1000, 30000000)
        self.check(['-30000'] * 1000, -30000000)
        self.check(['0'] + ['D'] * 999, 0)
        self.check(['1', 'C'] * 500, 0)
        self.check(['30000'] + ['D'] * 15, 30000 * (2**16 - 1))
        self.check(['5', '2', 'C', 'D', '+'], 30)
        self.check(['5', '-2', '4', 'C', 'D', '9', '+', '+'], 27)


if __name__ == '__main__':
    unittest.main()
