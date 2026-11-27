# 1038. Binary Search Tree to Greater Sum Tree · Python

[原题](https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/)。

BST值唯一，右根左遍历按原值从大到小访问。处理当前节点时total已是所有严格更大原值之和，先加入当前原值，再把该累积和写回，恰是题目要求的不小于自身值总和。后续走左边仍读取尚未改动的更小节点值，不受已写值影响。会原地修改节点值，返回同一根对象。

时间O(n)，显式栈空间O(h)，TreeNode由LeetCode提供。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
