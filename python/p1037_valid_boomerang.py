class Solution:
    def isBoomerang(self, points):
        first,second,third = points
        return ((second[0] - first[0]) * (third[1] - first[1])
                - (second[1] - first[1]) * (third[0] - first[0])) != 0
