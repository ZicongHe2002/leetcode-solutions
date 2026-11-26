from itertools import product
import re
import unittest

from python.p0468_validate_ip_address import Solution


OCTET = r'(?:0|[1-9][0-9]?|1[0-9]{2}|2[0-4][0-9]|25[0-5])'
IPV4 = re.compile(rf'{OCTET}(?:\.{OCTET}){{3}}')
IPV6 = re.compile(r'[0-9a-fA-F]{1,4}(?::[0-9a-fA-F]{1,4}){7}')


def grammar_oracle(text):
    if IPV4.fullmatch(text):
        return 'IPv4'
    if IPV6.fullmatch(text):
        return 'IPv6'
    return 'Neither'


class IpGrammarTests(unittest.TestCase):
    def check(self, text, expected=None):
        self.assertEqual(Solution().validIPAddress(text), grammar_oracle(text) if expected is None else expected)

    def test_all_ipv4_candidate_segments_against_full_grammar(self):
        segments = ('', '0', '00', '01', '1', '9', '10', '99', '100', '249', '255', '256', 'a')
        addresses = 0
        for parts in product(segments, repeat=4):
            self.check('.'.join(parts))
            addresses += 1
        self.assertEqual(addresses, 28561)
        for parts in product(('0', '255'), repeat=4):
            self.check('.'.join(parts), 'IPv4')

    def test_ipv6_per_position_segments_counts_and_forbidden_notations(self):
        segments = ('', '0', '0000', '00000', 'f', 'F', 'aBcD', 'ffff', 'FFFF', 'g', '+1', ' 1', '1.0')
        for index in range(8):
            for part in segments:
                address = ['aBcD'] * 8
                address[index] = part
                self.check(':'.join(address))
        for count in range(11):
            self.check(':'.join(['1'] * count))
        for address in ('', '::1', '::', '2001:db8::1', '::ffff:192.0.2.1',
                        '1:2:3:4:5:6:7:8/64', '1:2:3:4:5:6:7:8%eth0',
                        '1.2.3.4\n', '1.2.3.+4', '１.2.3.4', '1:2:3:4:5:6:7:８',
                        '1.2.3', '1.2.3.4.', '1..2.3.4'):
            self.check(address, 'Neither')
        self.check('2001:0db8:85a3:0:0:8A2E:0370:7334', 'IPv6')


if __name__ == '__main__':
    unittest.main()
