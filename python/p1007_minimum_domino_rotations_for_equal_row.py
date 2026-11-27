class Solution:
    def minDominoRotations(self, tops, bottoms):
        def rotations(value):
            top_moves = bottom_moves = 0
            for top,bottom in zip(tops,bottoms):
                if top != value and bottom != value:
                    return float('inf')
                top_moves += top != value
                bottom_moves += bottom != value
            return min(top_moves,bottom_moves)

        best = min(rotations(tops[0]),rotations(bottoms[0]))
        return -1 if best == float('inf') else best
