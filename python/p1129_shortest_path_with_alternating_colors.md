# 1129. Shortest Path with Alternating Colors · Python

[原题](https://leetcode.com/problems/shortest-path-with-alternating-colors/)。

有向图允许自环和重复边。到同一个节点但末边颜色不同，后续可用边不同，必须保留两个状态。起点同时以两种虚拟末色入队，使第一步可用任意颜色；每步只走另一种颜色。BFS第一次访问某状态即取得其最短边数，最终取每个节点两个可达状态的较小值。

时间和空间O(n+r+b)，r、b为两类边数。输入边列表保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
