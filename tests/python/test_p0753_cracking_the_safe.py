import unittest
from itertools import product

from python.p0753_cracking_the_safe import Solution


class CrackingSafeTests(unittest.TestCase):
    def test_every_legal_parameter_pair_against_complete_literal_password_set_and_length_lower_bound(self):
        checked = 0
        for n in range(1, 5):
            for k in range(1, 11):
                if k ** n > 4096:
                    continue
                alphabet = ''.join(map(str, range(k)))
                expected = {''.join(chars) for chars in product(alphabet, repeat=n)}
                result = Solution().crackSafe(n, k)
                self.assertIs(type(result), str)
                self.assertTrue(all(char in alphabet for char in result))
                self.assertEqual(len(result), k ** n + n - 1, (n, k))
                windows = [result[start:start + n] for start in range(len(result) - n + 1)]
                self.assertEqual(len(windows), len(expected))
                self.assertEqual(set(windows), expected, (n, k))
                checked += 1
        self.assertEqual(checked, 38)


if __name__ == '__main__':
    unittest.main()
