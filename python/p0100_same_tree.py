"""LeetCode 100: https://leetcode.com/problems/same-tree/."""

from __future__ import annotations


class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        pending = [(p, q)]
        while pending:
            first, second = pending.pop()
            if first is None or second is None:
                if first is not second:
                    return False
                continue
            if first.val != second.val:
                return False
            pending.append((first.right, second.right))
            pending.append((first.left, second.left))
        return True
