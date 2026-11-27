class Solution:
    def canTransform(self, start, end):
        size = len(start)
        first = second = 0
        while first < size or second < size:
            while first < size and start[first] == 'X':
                first += 1
            while second < size and end[second] == 'X':
                second += 1
            if first == size or second == size:
                return first == second
            if start[first] != end[second]:
                return False
            if start[first] == 'L' and first < second:
                return False
            if start[first] == 'R' and first > second:
                return False
            first += 1
            second += 1
        return True
