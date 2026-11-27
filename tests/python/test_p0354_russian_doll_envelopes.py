from itertools import product
import unittest

from python.p0354_russian_doll_envelopes import Solution


def subset_chain_oracle(envelopes):
    best = 0
    for mask in range(1 << len(envelopes)):
        chosen = sorted(envelopes[i] for i in range(len(envelopes)) if mask & (1 << i))
        if all(a[0] < b[0] and a[1] < b[1] for a, b in zip(chosen, chosen[1:])):
            best = max(best, len(chosen))
    return best


class EnvelopeStrictChainTests(unittest.TestCase):
    def check(self, envelopes, expected=None):
        before = [item[:] for item in envelopes]
        identities = [id(item) for item in envelopes]
        actual = Solution().maxEnvelopes(envelopes)
        self.assertIs(type(actual), int)
        self.assertEqual(actual, subset_chain_oracle(envelopes) if expected is None else expected)
        self.assertEqual(envelopes, before)
        self.assertEqual([id(item) for item in envelopes], identities)

    def test_all_small_ordered_inputs_against_every_subset(self):
        dimensions = tuple(product((1, 2, 3), repeat=2))
        inputs = 0
        for size in range(5):
            for envelopes in product(dimensions, repeat=size):
                self.check([list(item) for item in envelopes])
                inputs += 1
        self.assertEqual(inputs, 7381)

    def test_same_width_same_height_and_maximum_length(self):
        self.check([[5, 4], [6, 4], [6, 7], [2, 3]], 3)
        self.check([[2, 2], [2, 3]], 1)
        self.check([[i, i] for i in range(100000, 0, -1)], 100000)
        self.check([[1, i] for i in range(1, 100001)], 1)
        self.check([[i, 100000] for i in range(1, 100001)], 1)


if __name__ == '__main__':
    unittest.main()
