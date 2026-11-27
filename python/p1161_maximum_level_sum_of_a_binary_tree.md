# 1161. Maximum Level Sum of a Binary Tree · Python

[原题](https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/)。

根非空，层编号从1开始，节点值允许为负。每轮固定当前队列长度，只求这一层的和，孩子留到下一轮。最大和从负无穷初始化，防止全负树错误地返回未出现的零和层。平局保留最早层，因此只在严格更大时更新。

时间O(n)，队列额外空间O(w)，w为最大层宽，不修改树，TreeNode由LeetCode提供。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
