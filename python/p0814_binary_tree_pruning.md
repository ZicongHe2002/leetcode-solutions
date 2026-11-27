# 814. Binary Tree Pruning · Python

[原题](https://leetcode.com/problems/binary-tree-pruning/)。

节点值为0或1，要移除不含1的子树。先递归剪左右子树；若当前值为0且两棵处理后的子树都为空，整个当前子树都没有1，返回None。否则当前值或至少一个保留孩子含1，保留节点。后序使只含0的长链可以从叶子逐步剪到根。

使用LeetCode提供的TreeNode，原地更新保留节点的左右指针。时间O(n)，递归栈O(h)，h为树高。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
