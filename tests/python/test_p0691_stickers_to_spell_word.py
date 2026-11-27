import random
import unittest
from collections import deque
from itertools import combinations, product

from python.p0691_stickers_to_spell_word import Solution


def possible_assignments(mask, word, target):
    states = {mask}
    for char in word:
        states |= {state | (1 << i) for state in states for i, letter in enumerate(target)
                   if char == letter and not state & (1 << i)}
    return states


def position_assignment_bfs(stickers, target):
    complete = (1 << len(target)) - 1
    pending, visited = deque([(0, 0)]), {0}
    while pending:
        mask, used = pending.popleft()
        if mask == complete:
            return used
        for sticker in stickers:
            for following in possible_assignments(mask, sticker, target):
                if following not in visited:
                    visited.add(following)
                    pending.append((following, used + 1))
    return -1


class StickersWordTests(unittest.TestCase):
    def check(self, stickers, target, expected=None):
        before = stickers[:]
        result = Solution().minStickers(stickers, target)
        self.assertIs(type(result), int)
        self.assertEqual(result, position_assignment_bfs(stickers, target) if expected is None else expected,
                         (stickers, target))
        self.assertEqual(stickers, before)

    def test_small_sticker_sets_targets_and_assignments_against_mask_bfs(self):
        words = [''.join(chars) for size in (1, 2) for chars in product('ab', repeat=size)]
        targets = [''.join(chars) for size in range(1, 6) for chars in product('ab', repeat=size)]
        sets = checked = 0
        for count in range(1, 4):
            for selected in combinations(words, count):
                sets += 1
                for target in targets:
                    self.check(list(selected), target)
                    checked += 1
        self.assertEqual((sets, checked), (41, 2542))
        rng = random.Random(691)
        pool = [''.join(chars) for size in range(1, 4) for chars in product('abc', repeat=size)]
        for _ in range(200):
            selected = rng.sample(pool, rng.randrange(1, 5))
            target = ''.join(rng.choice('abc') for _ in range(rng.randrange(1, 8)))
            self.check(selected, target)

    def test_fifty_types_ten_character_stickers_and_fifteen_character_targets(self):
        stickers = ['a' * 9 + chr(97 + i) for i in range(26)]
        stickers += ['b' * 9 + chr(97 + i) for i in range(24)]
        self.assertEqual(len(set(stickers)), 50)
        self.check(stickers, 'a' * 15, 2)
        self.check(list('abcdefghijklmno'), 'abcdefghijklmno', 15)
        self.check(['ab'], 'a' * 7 + 'b' * 8, 8)
        self.check(['aa', 'bb'], 'a' * 7 + 'b' * 8, 8)
        self.check(['a' * 10, 'b' * 10], 'a' * 14 + 'c', -1)
        self.check(['with', 'example', 'science'], 'thehat', 3)
        self.check(['notice', 'possible'], 'basicbasic', -1)


if __name__ == '__main__':
    unittest.main()
