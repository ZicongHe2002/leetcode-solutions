# 938. Range Sum of BST · Python

[原题](https://leetcode.com/problems/range-sum-of-bst/)。

闭区间内节点值直接累计。BST节点值唯一，当前值不大于low时，左子树全更小，可剪掉；当前值不小于high时，右子树全更大，也可剪掉。其余方向迭代压栈，避免依赖深树递归。TreeNode由LeetCode提供，原树不修改。

最坏时间O(n)，显式DFS栈空间O(h)，h为树高；剪枝只减少实际访问量，不宣称最坏为对数时间。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
