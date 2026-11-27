# 1162. As Far from Land as Possible · Python

[原题](https://leetcode.com/problems/as-far-from-land-as-possible/)。

方阵中1是陆地、0是海洋，距离为曼哈顿距离。所有陆地作为距离0的源点，向四邻格同时扩展；BFS首次到达某海洋格即为它离任意陆地的最小距离。取所有新到达海洋格距离的最大值，得到距离陆地最远的海洋。全陆或全海按题意返回-1。

时间O(n^2)，额外空间O(n^2)，使用独立距离矩阵保持输入。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
