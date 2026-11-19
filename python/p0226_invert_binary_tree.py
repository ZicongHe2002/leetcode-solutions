"""LeetCode 226: https://leetcode.com/problems/invert-binary-tree/."""

from __future__ import annotations


class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        # TreeNode is supplied by the judge; keep the original nodes and root.
        if root is None:
            return None
        pending = [root]
        while pending:
            node = pending.pop()
            node.left, node.right = node.right, node.left
            if node.left is not None:
                pending.append(node.left)
            if node.right is not None:
                pending.append(node.right)
        return root
