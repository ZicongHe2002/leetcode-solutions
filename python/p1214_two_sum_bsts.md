# 1214. Two Sum BSTs · Python

[原题](https://leetcode.com/problems/two-sum-bsts/)。

题目要求各从两棵BST取一个节点，总和等于target。第一棵树建值集合，第二棵树逐节点检查target-node.val，命中就确定有合法跨树配对。本实现不依赖BST排序性质，重复值也可正确处理，不会在同一棵树内部错误配对。两次遍历使用显式栈，避免偏斜树递归深度问题。

期望时间O(n1+n2)，额外空间O(n1+h2)，最坏O(n1+n2)，两树不修改。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
