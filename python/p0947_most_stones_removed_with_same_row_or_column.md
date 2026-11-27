# 947. Most Stones Removed with Same Row or Column · Python

[原题](https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/)。

同行或同列石头可互相连接，每个连通分量至少留一块，沿生成树从叶部移除可以恰好只留一块，所以最多移除总数减分量数。用带r/c标签的行列二部图表达连接，每块石头合并对应行列节点，避免比较所有石头对。每个出现过的分量都含石头边，从各石头行节点根去重即可计分量；行号和列号即使数值相同也不会误合并。

按大小合并与路径压缩，期望时间O(n alpha(n))，额外空间O(n)，输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
