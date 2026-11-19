"""LeetCode 112: https://leetcode.com/problems/path-sum/."""

from __future__ import annotations


class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if root is None:
            return False
        pending = [(root, root.val)]
        while pending:
            node, total = pending.pop()
            if node.left is None and node.right is None:
                if total == targetSum:
                    return True
                continue
            if node.left is not None:
                pending.append((node.left, total + node.left.val))
            if node.right is not None:
                pending.append((node.right, total + node.right.val))
        return False
