from itertools import combinations, product
import unittest

from python.p1202_smallest_string_with_swaps import Solution


def all_swap_states(text, pairs):
    seen, pending = {text}, [text]
    while pending:
        current = pending.pop()
        for first, second in pairs:
            letters = list(current)
            letters[first], letters[second] = letters[second], letters[first]
            following = ''.join(letters)
            if following not in seen:
                seen.add(following)
                pending.append(following)
    return min(seen)


class SwapReachabilityTests(unittest.TestCase):
    def check(self, text, pairs, expected=None):
        before = [pair[:] for pair in pairs]
        if expected is None:
            expected = all_swap_states(text, pairs)
        result = Solution().smallestStringWithSwaps(text, pairs)
        self.assertIs(type(result), str)
        self.assertEqual(result, expected)
        self.assertEqual(pairs, before)

    def test_all_small_strings_and_swap_graphs_against_reachable_states(self):
        checks = 0
        for size in range(1, 5):
            possible = list(combinations(range(size), 2))
            for letters in product('abc', repeat=size):
                for mask in range(1 << len(possible)):
                    pairs = [list(pair) for index, pair in enumerate(possible) if mask >> index & 1]
                    self.check(''.join(letters), pairs)
                    checks += 1
        self.assertEqual(checks, 5421)

    def test_maximum_length_pairs_and_repeated_or_self_swaps(self):
        text = 'dcba' * 25000
        pairs = [[index, index + 1] for index in range(99999)] + [[0, 0]]
        self.check(text, pairs, ''.join(sorted(text)))
        self.check(text, [], text)
        self.check('dcab', [[0, 3], [0, 3], [1, 1]])
        self.check('z', [[0, 0]])


if __name__ == '__main__':
    unittest.main()
