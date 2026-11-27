# 863. All Nodes Distance K in Binary Tree · Python

[原题](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/)。

从target出发，最短路可能先向父方向，不能只搜索其子树。迭代遍历原树记录每个节点父亲，使每点最多有左右孩子加父亲三条无向邻边。然后从target做k层BFS，已见集合阻止往回走；完成后队列中恰是距离k的节点。k=0直接保留target，搜索耗尽则返回空表。LeetCode提供TreeNode，按节点身份记录父边，不修改原树。

时间O(n)，额外空间O(n)。结果顺序任意。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
