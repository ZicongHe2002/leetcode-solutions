import random
import unittest
from fractions import Fraction
from itertools import combinations
from math import isqrt

from python.p0786_k_th_smallest_prime_fraction import Solution


def all_exact_ranked_pairs(values):
    return sorted((Fraction(values[left],values[right]),values[left],values[right])
                  for left in range(len(values)) for right in range(left + 1,len(values)))


def primes_up_to(limit):
    return [value for value in range(2,limit + 1)
            if all(value % divisor for divisor in range(2,isqrt(value) + 1))]


class PrimeFractionTests(unittest.TestCase):
    def check(self, values, k, expected):
        before = values[:]
        result = Solution().kthSmallestPrimeFraction(values,k)
        self.assertIs(type(result),list)
        self.assertEqual(len(result),2)
        self.assertTrue(all(type(value) is int for value in result))
        self.assertEqual(result,list(expected),(values[:20],k))
        self.assertEqual(values,before)

    def test_every_rank_of_small_prime_subsets_against_all_exact_fraction_pairs(self):
        checked = 0
        for size in range(1,7):
            for chosen in combinations((2,3,5,7,11,13),size):
                values = [1] + list(chosen)
                for k,(_,numerator,denominator) in enumerate(all_exact_ranked_pairs(values),1):
                    self.check(values,k,(numerator,denominator))
                    checked += 1
        self.assertEqual(checked,432)

    def test_seeded_full_ranks_official_examples_and_maximum_length_and_denominator(self):
        rng = random.Random(786)
        small_primes = primes_up_to(300)
        for _ in range(100):
            values = [1] + sorted(rng.sample(small_primes,rng.randrange(1,25)))
            ranked = all_exact_ranked_pairs(values)
            k = rng.randrange(1,len(ranked) + 1)
            self.check(values,k,ranked[k-1][1:])
        self.check([1,2,3,5],3,(2,5))
        self.check([1,7],1,(1,7))
        primes = primes_up_to(30000)
        values = [1] + primes[:998] + [primes[-1]]
        self.assertEqual(len(values),1000)
        self.check(values,1,(1,values[-1]))
        largest = max(((values[left],values[right]) for left in range(1000) for right in range(left + 1,1000)),
                      key=lambda pair: Fraction(*pair))
        self.check(values,1000 * 999 // 2,largest)


if __name__ == '__main__':
    unittest.main()
