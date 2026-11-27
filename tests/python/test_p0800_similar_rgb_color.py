import random
import unittest
from itertools import product

from python.p0800_similar_rgb_color import Solution


def channels(color):
    return tuple(int(color[offset:offset + 2],16) for offset in (1,3,5))


class SimilarRGBTests(unittest.TestCase):
    def check(self, color):
        result = Solution().similarRGB(color)
        self.assertIs(type(result),str)
        self.assertEqual(len(result),7)
        self.assertEqual(result[0],'#')
        self.assertTrue(all(char in '0123456789abcdef' for char in result[1:]))
        self.assertTrue(all(result[index] == result[index + 1] for index in (1,3,5)))
        return result

    def test_every_channel_value_against_all_sixteen_channel_choices(self):
        checked = 0
        for channel in range(3):
            for value in range(256):
                values = [85,170,51]
                values[channel] = value
                result = channels(self.check('#' + ''.join(format(item,'02x') for item in values)))
                expected = tuple(min(range(0,256,17),key=lambda candidate:(candidate - item)**2) for item in values)
                self.assertEqual(result,expected)
                checked += 1
        self.assertEqual(checked,768)

    def test_full_rgb_search_examples_and_rounding_boundaries(self):
        generator = random.Random(800)
        colors = ['#09f166','#4e3fe1','#000000','#ffffff','#080909','#f6f7f8']
        colors += ['#' + format(generator.randrange(1 << 24),'06x') for _ in range(26)]
        self.assertEqual(len(colors),32)
        for color in colors:
            original = channels(color)
            result = channels(self.check(color))
            cost = sum((a - b)**2 for a,b in zip(original,result))
            optimum = min(sum((a - b)**2 for a,b in zip(original,candidate))
                          for candidate in product(range(0,256,17),repeat=3))
            self.assertEqual(cost,optimum,color)
        self.assertEqual(self.check('#09f166'),'#11ee66')
        self.assertEqual(self.check('#4e3fe1'),'#5544dd')


if __name__ == '__main__':
    unittest.main()
