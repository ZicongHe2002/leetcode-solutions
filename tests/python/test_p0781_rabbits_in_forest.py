import unittest
from itertools import product

from python.p0781_rabbits_in_forest import Solution


def actual_respondent_partitions(answers):
    best = sum(answer + 1 for answer in answers)

    def visit(index, blocks):
        nonlocal best
        if index == len(answers):
            best = min(best, sum(answer + 1 for answer, _ in blocks))
            return
        answer = answers[index]
        for block in blocks:
            if block[0] == answer and block[1] < answer + 1:
                block[1] += 1
                visit(index + 1, blocks)
                block[1] -= 1
        blocks.append([answer,1])
        visit(index + 1, blocks)
        blocks.pop()

    visit(0,[])
    return best


class RabbitsForestTests(unittest.TestCase):
    def check(self, answers, expected=None):
        before = answers[:]
        result = Solution().numRabbits(answers)
        self.assertIs(type(result), int)
        self.assertEqual(result, actual_respondent_partitions(answers) if expected is None else expected, answers[:20])
        self.assertEqual(answers,before)

    def test_all_small_answer_arrays_against_actual_uniform_capacity_set_partitions(self):
        checked = 0
        for size in range(1,8):
            for answers in product(range(3),repeat=size):
                self.check(list(answers))
                checked += 1
        self.assertEqual(checked,3279)

    def test_official_examples_maximum_reports_and_group_capacity_edges(self):
        self.check([1,1,2],5)
        self.check([10,10,10],11)
        self.check([0] * 1000,1000)
        self.check([999] * 1000,1000)
        self.check([998] * 1000,1998)
        self.check([1] * 999,1000)
        self.check([999],1000)
        self.check(list(range(1000)),500500)
        self.check([2,2,2],3)
        self.check([2,2,2,2],6)


if __name__ == '__main__':
    unittest.main()
