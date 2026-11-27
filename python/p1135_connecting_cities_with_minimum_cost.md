# 1135. Connecting Cities With Minimum Cost · Python

[原题](https://leetcode.com/problems/connecting-cities-with-minimum-cost/)。

城市编号1..n，连接为无向带权边。按代价递增选取跨分量边，每次选取都是当前割上的最小可用边，可被纳入某棵最小生成树；同分量边只会成环，跳过。所有边处理后仍有多个分量则无法连接全部城市，返回-1；单城市无需边，代价0。

边数m，时间O(m log m+(n+m)alpha(n))，额外空间O(n+m)，排序使用副本。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
