from collections import deque
import unittest

from python.p0397_integer_replacement import Solution


def original_operation_bfs(n):
    queue = deque([(n, 0)])
    seen = {n}
    while queue:
        value, distance = queue.popleft()
        if value == 1:
            return distance
        neighbors = (value // 2,) if value % 2 == 0 else (value - 1, value + 1)
        for neighbor in neighbors:
            if 1 <= neighbor <= n + 1 and neighbor not in seen:
                seen.add(neighbor)
                queue.append((neighbor, distance + 1))
    raise AssertionError('positive integer must reach one')


class ReplacementShortestPathTests(unittest.TestCase):
    def check(self, n, expected=None):
        actual = Solution().integerReplacement(n)
        self.assertIs(type(actual), int)
        self.assertEqual(actual, original_operation_bfs(n) if expected is None else expected)

    def test_all_small_integers_against_original_operation_graph(self):
        for n in range(1, 4097):
            self.check(n)

    def test_binary_neighbors_and_signed_32_bit_maximum(self):
        self.check(1, 0)
        self.check(3, 2)
        self.check(7, 4)
        for power in range(1, 31):
            self.check((1 << power) - 1)
            self.check(1 << power, power)
            self.check((1 << power) + 1)
        self.check(2**31 - 1, 32)


if __name__ == '__main__':
    unittest.main()
