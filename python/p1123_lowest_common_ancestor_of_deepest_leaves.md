# 1123. Lowest Common Ancestor of Deepest Leaves · Python

[原题](https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/)。

每个子树返回高度以及其最深叶子的最低公共祖先。左右高度相等时，两边最深叶子都属于当前最深层，公共祖先就是当前节点；一侧更高时，最深叶子全部来自较高侧，沿用该侧祖先。叶子的两边空高度相等，正确返回叶子自身。显式后序栈保证访问当前节点时孩子结果已计算，不使用容易在深树溢出的递归。

时间O(n)，额外空间O(n)，不修改树，返回原树节点，TreeNode由LeetCode提供。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
