class Solution:
    def intersect(self, quadTree1, quadTree2):
        if quadTree1.isLeaf:
            if quadTree1.val:
                return Node(True, True, None, None, None, None)
            return quadTree2
        if quadTree2.isLeaf:
            if quadTree2.val:
                return Node(True, True, None, None, None, None)
            return quadTree1
        children = [
            self.intersect(quadTree1.topLeft, quadTree2.topLeft),
            self.intersect(quadTree1.topRight, quadTree2.topRight),
            self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft),
            self.intersect(quadTree1.bottomRight, quadTree2.bottomRight),
        ]
        if all(child.isLeaf for child in children) and all(child.val == children[0].val for child in children):
            return Node(bool(children[0].val), True, None, None, None, None)
        return Node(False, False, *children)
