from itertools import islice, product
import unittest

from python.p0458_poor_pigs import Solution


def simulated_observations(buckets, rounds, pigs):
    labels = list(islice(product(range(rounds + 1), repeat=pigs), buckets))
    if len(labels) != buckets:
        raise AssertionError('not enough distinguishable bucket labels')
    feed = {}
    for bucket, label in enumerate(labels):
        for pig, round_number in enumerate(label):
            if round_number:
                feed.setdefault((pig, round_number), set()).add(bucket)
    signatures = []
    for poison in range(buckets):
        signature = []
        for pig in range(pigs):
            death = 0
            for round_number in range(1, rounds + 1):
                if poison in feed.get((pig, round_number), ()):
                    death = round_number
                    break
            signature.append(death)
        signatures.append(tuple(signature))
    return signatures


class PigRoundCapacityTests(unittest.TestCase):
    def check(self, buckets, die, test, expected=None):
        pigs = Solution().poorPigs(buckets, die, test)
        self.assertIs(type(pigs), int)
        self.assertGreaterEqual(pigs, 0)
        self.assertLessEqual(pigs, 10)
        if expected is not None:
            self.assertEqual(pigs, expected)
        rounds = test // die
        self.assertEqual(len(set(simulated_observations(buckets, rounds, pigs))), buckets)
        if pigs:
            fewer_labels = list(islice(product(range(rounds + 1), repeat=pigs - 1), buckets))
            self.assertLess(len(fewer_labels), buckets)

    def test_small_feeding_plans_with_unused_partial_round_time(self):
        plans = 0
        for rounds in range(1, 5):
            for buckets in range(1, 65):
                self.check(buckets, 2, 2 * rounds + 1)
                plans += 1
        self.assertEqual(plans, 256)

    def test_maximum_buckets_single_bucket_and_exact_power_neighbors(self):
        self.check(1000, 15, 60, 5)
        self.check(1000, 100, 100, 10)
        self.check(1, 1, 100, 0)
        for die, test in ((100, 100), (1, 2), (15, 60)):
            states = test // die + 1
            for exponent in range(1, 7):
                for buckets in (states**exponent - 1, states**exponent, states**exponent + 1):
                    if 1 <= buckets <= 1000:
                        self.check(buckets, die, test)


if __name__ == '__main__':
    unittest.main()
