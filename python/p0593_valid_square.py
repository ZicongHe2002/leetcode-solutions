class Solution:
    def validSquare(self, p1, p2, p3, p4):
        vectors = sorted(((point[0] - p1[0], point[1] - p1[1]) for point in (p2, p3, p4)),
                         key=lambda vector: vector[0] ** 2 + vector[1] ** 2)
        first, second, diagonal = vectors
        side = first[0] ** 2 + first[1] ** 2
        return (side > 0 and second[0] ** 2 + second[1] ** 2 == side
                and first[0] * second[0] + first[1] * second[1] == 0
                and diagonal == (first[0] + second[0], first[1] + second[1]))
