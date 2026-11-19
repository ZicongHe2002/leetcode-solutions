"""LeetCode 104: https://leetcode.com/problems/maximum-depth-of-binary-tree/."""

from __future__ import annotations

from collections import deque


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        # The judge supplies TreeNode. The queue only borrows node references.
        if root is None:
            return 0
        pending = deque([root])
        depth = 0
        while pending:
            depth += 1
            for _ in range(len(pending)):
                node = pending.popleft()
                if node.left is not None:
                    pending.append(node.left)
                if node.right is not None:
                    pending.append(node.right)
        return depth
