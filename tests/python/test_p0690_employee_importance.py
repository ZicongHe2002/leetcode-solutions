import unittest
from itertools import product

from python.p0690_employee_importance import Solution


class Employee:
    def __init__(self, id, importance, subordinates):
        self.id, self.importance, self.subordinates = id, importance, subordinates


def reachable_closure(employees, target):
    reachable = {target}
    while True:
        before = len(reachable)
        for employee in employees:
            if employee.id in reachable:
                reachable.update(employee.subordinates)
        if len(reachable) == before:
            return sum(employee.importance for employee in employees if employee.id in reachable)


class EmployeeImportanceTests(unittest.TestCase):
    def check(self, employees, target, expected=None):
        order = [id(employee) for employee in employees]
        before = [(employee, employee.id, employee.importance,
                   employee.subordinates, employee.subordinates[:]) for employee in employees]
        result = Solution().getImportance(employees, target)
        self.assertIs(type(result), int)
        self.assertEqual(result, reachable_closure(employees, target) if expected is None else expected)
        self.assertEqual([id(employee) for employee in employees], order)
        for employee, identifier, importance, subordinate_list, values in before:
            self.assertEqual((employee.id, employee.importance), (identifier, importance))
            self.assertIs(employee.subordinates, subordinate_list)
            self.assertEqual(employee.subordinates, values)

    def test_small_forests_sparse_ids_signed_values_and_all_queries_against_set_closure(self):
        identifiers = (7, 31, 83, 307, 1009, 1999)
        forests = checked = 0
        for size in range(1, 7):
            choices = [(-1,)] + [tuple(range(-1, i)) for i in range(1, size)]
            patterns = ([0] * size, [(-1)**i * (i + 1) for i in range(size)],
                        [-100 if i % 2 == 0 else 100 for i in range(size)])
            for parents in product(*choices):
                forests += 1
                for importance in patterns:
                    employees = [Employee(identifiers[i], importance[i], []) for i in range(size)]
                    for i, parent in enumerate(parents):
                        if parent >= 0:
                            employees[parent].subordinates.append(identifiers[i])
                    employees.reverse()
                    for target in identifiers[:size]:
                        self.check(employees, target)
                        checked += 1
        self.assertEqual((forests, checked), (873, 15117))

    def test_two_thousand_employees_deep_chain_wide_star_and_negative_leaf(self):
        chain = [Employee(i, -100, [i + 1] if i < 2000 else []) for i in range(1, 2001)]
        chain.reverse()
        self.check(chain, 1, -200000)
        self.check(chain, 1000, -100100)
        self.check(chain, 2000, -100)
        star = [Employee(i, 100, []) for i in range(1, 2000)]
        star.append(Employee(2000, 100, list(range(1, 2000))))
        self.check(star, 2000, 200000)
        self.check(star, 1, 100)
        self.check([Employee(1, 2, [5]), Employee(5, -3, [])], 5, -3)


if __name__ == '__main__':
    unittest.main()
