# 1026. Maximum Difference Between Node and Ancestor · Python

[原题](https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/)。

同一根到当前路径上的任意两节点都有祖先关系，路径最大值减最小值是该路径可能的最大绝对差。遍历时各分支携带自己的路径极值，加入当前节点后更新答案，再传给孩子。不能拿两条无祖先关系分支的全树最小最大值相减。显式栈处理深链，原树保持。

时间O(n)，栈空间O(h)，TreeNode由LeetCode提供。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
