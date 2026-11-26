from itertools import product
import unittest

from python.p0535_encode_and_decode_tinyurl import Codec


class TinyURLRoundTripTests(unittest.TestCase):
    def encode_receipts(self, codec, urls):
        receipts = []
        for url in urls:
            short = codec.encode(url)
            self.assertIs(type(short), str)
            self.assertTrue(short.startswith('http://tinyurl.com/'))
            self.assertEqual(codec.decode(short), url)
            receipts.append((short, url))
        owners = {}
        for short, url in receipts:
            if short in owners:
                self.assertEqual(owners[short], url)
            owners[short] = url
        return receipts

    def verify_receipts(self, codec, receipts):
        for short, url in reversed(receipts):
            self.assertEqual(codec.decode(short), url)

    def test_every_short_path_roundtrip_and_old_receipts_survive_reencoding(self):
        urls = ['https://example.com/' + ''.join(chars)
                for size in range(1, 6) for chars in product('abc', repeat=size)]
        self.assertEqual(len(urls), 363)
        codec = Codec()
        receipts = self.encode_receipts(codec, urls)
        self.assertEqual(len({short for short, _ in receipts}), len(urls))
        self.encode_receipts(codec, urls[::-1])
        self.verify_receipts(codec, receipts)

    def test_many_urls_maximum_length_exact_text_and_instance_isolation(self):
        codec = Codec()
        urls = [f'https://example.com/item/{index}?q={index}#part' for index in range(10000)]
        receipts = self.encode_receipts(codec, urls)
        self.assertEqual(len({short for short, _ in receipts}), 10000)
        base = 'https://example.com/'
        maximum = base + 'z' * (10000 - len(base))
        self.assertEqual(len(maximum), 10000)
        special = [maximum, 'https://Example.com/a%2Fb?x=1&x=2#part', 'http://tinyurl.com/0']
        extra = self.encode_receipts(codec, special)
        self.verify_receipts(codec, receipts + extra)
        first, second = Codec(), Codec()
        first_short = first.encode('https://example.com/first')
        second_short = second.encode('https://example.com/second')
        self.assertEqual(first.decode(first_short), 'https://example.com/first')
        self.assertEqual(second.decode(second_short), 'https://example.com/second')
        self.verify_receipts(codec, receipts + extra)


if __name__ == '__main__':
    unittest.main()
