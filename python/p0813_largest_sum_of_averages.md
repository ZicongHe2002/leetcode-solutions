# 813. Largest Sum of Averages · Python

[原题](https://leetcode.com/problems/largest-sum-of-averages/)。

题目数组为正数，要求至多k个非空连续组的平均值之和最大。把一个非单点正数组拆成两组，两个平均值之和大于原组合平均，因此最优可以取恰好k组。

best[end]为前end项分成当前组数的最优值。初始一组时为前缀平均；增加一组，枚举最后一组起点cut，取旧best[cut]与末段平均之和的最大值。每组另建数组，且cut至少是旧组数，保证组非空。前缀和使末段平均常数时间求得，输入不变。

时间O(k*n^2)，额外空间O(n)，结果为浮点数。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
