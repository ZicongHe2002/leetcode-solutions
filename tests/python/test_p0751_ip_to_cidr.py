import ipaddress
import random
import unittest
from functools import lru_cache

from python.p0751_ip_to_cidr import Solution


@lru_cache(None)
def all_aligned_block_choices(start, end):
    if start == end:
        return 0
    return min(1 + all_aligned_block_choices(start + size, end)
               for prefix in range(33) for size in (1 << (32 - prefix),)
               if size <= end - start and start % size == 0)


class IpToCidrTests(unittest.TestCase):
    def check(self, ip, count, minimum=None):
        first = int(ipaddress.IPv4Address(ip))
        end = first + count
        self.assertTrue(1 <= count <= 1000 and end <= 1 << 32)
        result = Solution().ipToCIDR(ip, count)
        self.assertIs(type(result), list)
        cursor = first
        for block in result:
            self.assertIs(type(block), str)
            network = ipaddress.IPv4Network(block, strict=True)
            self.assertEqual(int(network.network_address), cursor)
            cursor += network.num_addresses
            self.assertLessEqual(cursor, end)
        self.assertEqual(cursor, end)
        if minimum is None:
            reference = list(ipaddress.summarize_address_range(ipaddress.IPv4Address(first), ipaddress.IPv4Address(end - 1)))
            minimum = len(reference)
        self.assertEqual(len(result), minimum, (ip, count, result))

    def test_all_small_intervals_against_exhaustive_aligned_cover_choices(self):
        checked = 0
        for start in range(32):
            for count in range(1, 33):
                self.check(str(ipaddress.IPv4Address(start)), count, all_aligned_block_choices(start, start + count))
                checked += 1
        self.assertEqual(checked, 1024)

    def test_seeded_ipv4_ranges_official_examples_zero_and_upper_address_boundaries(self):
        rng = random.Random(751)
        for _ in range(1000):
            count = rng.randrange(1, 1001)
            start = rng.randrange((1 << 32) - count + 1)
            self.check(str(ipaddress.IPv4Address(start)), count)
        self.check('255.0.0.7', 10, 3)
        self.check('117.145.102.62', 8, 3)
        self.check('0.0.0.0', 1, 1)
        self.check('0.0.0.0', 512, 1)
        self.check('0.0.0.0', 1000)
        self.check('0.0.0.255', 10)
        self.check('255.255.255.255', 1, 1)
        self.check(str(ipaddress.IPv4Address((1 << 32) - 1000)), 1000)


if __name__ == '__main__':
    unittest.main()
