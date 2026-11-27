# 1043. Partition Array for Maximum Sum · Python

[原题](https://leetcode.com/problems/partition-array-for-maximum-sum/)。

每个非空分段长度至多k，替换后该段贡献为段长乘原最大值。best[end]表示前end项的最优贡献，枚举最后一段长度1..min(k,end)，从右向左扩段时更新最大值，再加best[end-length]。枚举覆盖每个合法最后分段，更早部分已最优，因此得到全局最优，不能只按局部最大值贪心切段。

时间O(nk)，额外空间O(n)，原题非负数，初始最大值0与空前缀0正确，输入不修改。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
