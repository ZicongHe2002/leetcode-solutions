import unittest
from itertools import permutations, product

from python.p0803_bricks_falling_when_hit import Solution


def literal_forward_erasures(grid, hits):
    board = [row[:] for row in grid]
    rows,columns = len(board),len(board[0])

    def stable():
        reached = {(0,column) for column in range(columns) if board[0][column]}
        todo = list(reached)
        for row,column in todo:
            for dr,dc in ((-1,0),(1,0),(0,-1),(0,1)):
                nr,nc = row + dr,column + dc
                if 0 <= nr < rows and 0 <= nc < columns and board[nr][nc] and (nr,nc) not in reached:
                    reached.add((nr,nc))
                    todo.append((nr,nc))
        return reached

    result = []
    for row,column in hits:
        if not board[row][column]:
            result.append(0)
            continue
        before = stable()
        board[row][column] = 0
        fallen = before - stable() - {(row,column)}
        for nr,nc in fallen:
            board[nr][nc] = 0
        result.append(len(fallen))
    return result


class BricksFallingTests(unittest.TestCase):
    def check(self, grid, hits, expected=None):
        before = [row[:] for row in grid],[point[:] for point in hits]
        if expected is None:
            expected = literal_forward_erasures(grid,hits)
        result = Solution().hitBricks(grid,hits)
        self.assertEqual(result,expected,(grid,hits))
        self.assertTrue(all(type(value) is int for value in result))
        self.assertEqual((grid,hits),before)

    def test_all_small_grids_and_unique_hit_orders_against_actual_forward_stability(self):
        checked = 0
        for rows,columns in ((1,1),(1,2),(2,2),(2,3)):
            points = list(product(range(rows),range(columns)))
            for cells in product((0,1),repeat=rows * columns):
                grid = [list(cells[row * columns:(row + 1) * columns]) for row in range(rows)]
                for length in range(1,min(3,len(points)) + 1):
                    for hits in permutations(points,length):
                        self.check(grid,[list(point) for point in hits])
                        checked += 1
        self.assertEqual(checked,10642)

    def test_examples_roof_disconnect_and_maximum_grid_hit_limits(self):
        self.check([[1,0,0,0],[1,1,1,0]],[[1,0]],[2])
        self.check([[1,0,0,0],[1,1,0,0]],[[1,1],[1,0]],[0,0])
        self.check([[1] * 200 for _ in range(200)],[[0,column] for column in range(200)],[0] * 199 + [39800])
        self.check([[0] * 200 for _ in range(200)],[[row,column] for row in range(200) for column in range(200)],[0] * 40000)
        self.check([[1] for _ in range(200)],[[0,0],[199,0]],[199,0])
        self.check([[0,1],[1,0]],[[0,1]],[0])


if __name__ == '__main__':
    unittest.main()
