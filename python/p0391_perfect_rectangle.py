class Solution:
    def isRectangleCover(self, rectangles):
        if not rectangles:
            return False
        left, bottom, right, top = rectangles[0]
        area = 0
        corners = set()
        for x1, y1, x2, y2 in rectangles:
            if x1 >= x2 or y1 >= y2:
                return False
            left, bottom = min(left, x1), min(bottom, y1)
            right, top = max(right, x2), max(top, y2)
            area += (x2 - x1) * (y2 - y1)
            for point in ((x1, y1), (x1, y2), (x2, y1), (x2, y2)):
                if point in corners:
                    corners.remove(point)
                else:
                    corners.add(point)
        outer = {(left, bottom), (left, top), (right, bottom), (right, top)}
        return area == (right - left) * (top - bottom) and corners == outer
