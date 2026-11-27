import heapq
import unittest

from python.p0264_ugly_number_ii import Solution


def deduplicated_heap_sequence(length):
    pending = [1]
    discovered = {1}
    output = []
    for _ in range(length):
        current = heapq.heappop(pending)
        output.append(current)
        for factor in (2, 3, 5):
            candidate = current * factor
            if candidate not in discovered:
                discovered.add(candidate)
                heapq.heappush(pending, candidate)
    return output


class ThreeSequenceUglyNumberTests(unittest.TestCase):
    def check(self, n, expected):
        result = Solution().nthUglyNumber(n)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)

    def test_every_legal_index_against_deduplicated_heap_generation(self):
        reference = deduplicated_heap_sequence(1690)
        for n, expected in enumerate(reference, 1):
            self.check(n, expected)

    def test_initial_sequence_tied_candidates_and_maximum_index(self):
        first_ten = (1, 2, 3, 4, 5, 6, 8, 9, 10, 12)
        for n, expected in enumerate(first_ten, 1):
            self.check(n, expected)
        self.check(18, 30)
        self.check(1690, 2123366400)


if __name__ == '__main__':
    unittest.main()
