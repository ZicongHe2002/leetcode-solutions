"""LeetCode 101: https://leetcode.com/problems/symmetric-tree/."""

from __future__ import annotations

from collections import deque


class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        if root is None:
            return True
        pending = deque([(root.left, root.right)])
        while pending:
            left, right = pending.popleft()
            if left is None or right is None:
                if left is not right:
                    return False
                continue
            if left.val != right.val:
                return False
            pending.append((left.left, right.right))
            pending.append((left.right, right.left))
        return True
