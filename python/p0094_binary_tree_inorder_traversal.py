"""LeetCode 94: https://leetcode.com/problems/binary-tree-inorder-traversal/."""

from __future__ import annotations


class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        # TreeNode is supplied by LeetCode; nodes are borrowed and never changed.
        result = []
        pending = []
        current = root
        while current is not None or pending:
            while current is not None:
                pending.append(current)
                current = current.left
            current = pending.pop()
            result.append(current.val)
            current = current.right
        return result
