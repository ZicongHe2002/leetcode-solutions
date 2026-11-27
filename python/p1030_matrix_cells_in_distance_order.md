# 1030. Matrix Cells in Distance Order · Python

[原题](https://leetcode.com/problems/matrix-cells-in-distance-order/)。

没有障碍的矩形网格里，四向最短步数正好等于行差绝对值加列差绝对值。以给定中心BFS，首次入队就标记，保证每格仅出现一次；出队按最短距离分层，所以输出满足距离非递减，同距离格的任意顺序都合法。不需要先算距离再比较排序。

R行C列，时间和额外空间O(RC)，包含输出、队列与已见集合。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
