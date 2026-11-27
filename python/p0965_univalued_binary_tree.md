# 965. Univalued Binary Tree · Python

[原题](https://leetcode.com/problems/univalued-binary-tree/)。

题目给定非空树，若整树单值，该值一定等于根值。显式栈遍历每个节点，遇到不同值直接失败，全部相同则成功。无需收集全部值集合，也不修改节点链接。TreeNode由LeetCode提供。

最坏时间O(n)，DFS栈额外空间O(h)，h为树高。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
