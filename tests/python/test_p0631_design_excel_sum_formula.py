import random
import re
import unittest

from python.p0631_design_excel_sum_formula import Excel


class EagerSheet:
    def __init__(self, height, width):
        self.height, self.width = height, width
        self.definitions = [0] * (height * width)
        self.values = self.definitions[:]

    def index(self, row, column):
        return (row - 1) * self.width + ord(column) - ord('A')

    def replace(self, row, column, definition):
        if isinstance(definition, list):
            expanded = []
            for term in definition:
                coordinates = re.findall(r'([A-Z])([0-9]+)', term)
                left, top = coordinates[0][0], int(coordinates[0][1])
                right, bottom = coordinates[-1][0], int(coordinates[-1][1])
                for r in range(top, bottom + 1):
                    for c in range(ord(left), ord(right) + 1):
                        expanded.append(self.index(r, chr(c)))
            definition = expanded
        target = self.index(row, column)
        self.definitions[target] = definition
        for index, stored in enumerate(self.definitions):
            self.values[index] = (sum(self.values[source] for source in stored)
                                  if isinstance(stored, list) else stored)
        return self.values[target]


class ExcelFormulaTests(unittest.TestCase):
    def test_fifty_hundred_operation_programs_against_eager_recomputation(self):
        rng = random.Random(631)
        calls = 0
        for _ in range(50):
            actual = Excel(5, 'E')
            oracle = EagerSheet(5, 5)
            for _ in range(100):
                index = rng.randrange(25)
                row, column = index // 5 + 1, chr(ord('A') + index % 5)
                action = rng.choice(('get', 'set', 'sum')) if index else 'set'
                if action == 'set':
                    value = rng.randint(-100, 100)
                    self.assertIsNone(actual.set(row, column, value))
                    oracle.replace(row, column, value)
                elif action == 'get':
                    self.assertEqual(actual.get(row, column), oracle.values[index])
                else:
                    terms = []
                    for _ in range(rng.randint(1, 5)):
                        if row > 1 and rng.randrange(2):
                            top, bottom = sorted((rng.randrange(1, row), rng.randrange(1, row)))
                            left, right = sorted((rng.randrange(5), rng.randrange(5)))
                            terms.append(f"{chr(65 + left)}{top}:{chr(65 + right)}{bottom}")
                        else:
                            source = rng.randrange(index)
                            terms.append(f"{chr(65 + source % 5)}{source // 5 + 1}")
                    self.assertEqual(actual.sum(row, column, terms),
                                     oracle.replace(row, column, terms))
                calls += 1
        self.assertEqual(calls, 5000)

    def test_overlaps_duplicate_references_and_formula_replacement(self):
        sheet = Excel(26, 'Z')
        self.assertEqual(sheet.get(26, 'Z'), 0)
        sheet.set(1, 'A', 100)
        sheet.set(26, 'Y', -100)
        sheet.set(1, 'Z', 75)
        self.assertEqual(sheet.sum(26, 'Z', ['A1:Z25', 'A1:Y26']), 175)
        sheet.set(1, 'A', -100)
        self.assertEqual(sheet.get(26, 'Z'), -225)
        self.assertEqual(sheet.sum(26, 'Z', ['A1'] * 5), -500)
        self.assertEqual(sheet.sum(1, 'A', ['B1']), 0)
        sheet.set(1, 'B', 7)
        self.assertEqual(sheet.get(26, 'Z'), 35)
        sheet.set(26, 'Z', 3)
        sheet.set(1, 'B', 100)
        self.assertEqual(sheet.get(26, 'Z'), 3)

    def test_maximum_dimensions_and_97_cell_dependency_chain(self):
        sheet = Excel(26, 'Z')
        cells = [(index // 26 + 1, chr(65 + index % 26)) for index in range(96)]
        cells.append((26, 'Z'))
        sheet.set(*cells[0], 3)
        for previous, current in zip(cells, cells[1:]):
            reference = f'{previous[1]}{previous[0]}'
            self.assertEqual(sheet.sum(*current, [reference]), 3)
        sheet.set(*cells[0], -100)
        self.assertEqual(sheet.get(*cells[-1]), -100)


if __name__ == '__main__':
    unittest.main()
