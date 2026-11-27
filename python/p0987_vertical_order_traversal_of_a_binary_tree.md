# 987. Vertical Order Traversal of a Binary Tree · Python

[原题](https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/)。

根坐标(行0,列0)，左孩子列减1、右孩子列加1，两者行都加1。遍历收集(列,行,值)三元组后整体排序，恰好实现列从左到右、列内从上到下、相同行列按值升序的规则。再按列分组，不依赖DFS访问同坐标节点时的先后。

时间O(n log n)，额外空间O(n)，原树保持，TreeNode由LeetCode提供。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
