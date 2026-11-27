class Solution:
    def splitBST(self, root, target):
        small = small_tail = None
        large = large_tail = None
        node = root
        while node:
            if node.val <= target:
                if small_tail:
                    small_tail.right = node
                else:
                    small = node
                small_tail = node
                node = node.right
                small_tail.right = None
            else:
                if large_tail:
                    large_tail.left = node
                else:
                    large = node
                large_tail = node
                node = node.left
                large_tail.left = None
        return [small, large]
