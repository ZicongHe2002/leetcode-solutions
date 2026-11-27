from itertools import product
import unittest

from python.p0465_optimal_account_balancing import Solution


def recursive_payment_oracle(transactions):
    net = [0] * 12
    for sender, receiver, amount in transactions:
        net[sender] -= amount
        net[receiver] += amount

    def settle(values):
        values = tuple(value for value in values if value)
        if not values:
            return 0
        best = len(values) - 1
        for index in range(1, len(values)):
            if values[0] * values[index] < 0:
                following = list(values[1:])
                following[index - 1] += values[0]
                best = min(best, 1 + settle(following))
        return best

    return settle(net)


class MaximumZeroSumGroupingTests(unittest.TestCase):
    def check(self, transactions, expected=None):
        before = [item[:] for item in transactions]
        actual = Solution().minTransfers(transactions)
        self.assertIs(type(actual), int)
        self.assertEqual(actual, recursive_payment_oracle(transactions) if expected is None else expected)
        self.assertEqual(transactions, before)

    def test_all_small_transaction_programs_against_payment_search(self):
        actions = tuple((sender, receiver, amount) for sender in range(4) for receiver in range(4)
                        if sender != receiver for amount in (1, 2))
        programs = 0
        for length in range(1, 4):
            for transactions in product(actions, repeat=length):
                self.check([list(item) for item in transactions])
                programs += 1
        self.assertEqual(programs, 14424)
        self.check([], 0)

    def test_maximum_people_transaction_count_amount_and_zero_subgroups(self):
        self.check([[2 * index, 2 * index + 1, index + 1] for index in range(6)], 6)
        self.check([[index, index + 1, 100] for index in range(8)], 1)
        self.check([[0, 1, 10], [1, 0, 10]], 0)
        self.check([[0, 3, 3], [1, 3, 1], [1, 4, 2], [2, 4, 3]], 4)
        self.check([[0, 4, 1], [1, 4, 2], [2, 5, 4], [3, 5, 5]], 4)


if __name__ == '__main__':
    unittest.main()
