# 871. Minimum Number of Refueling Stops · Python

[原题](https://leetcode.com/problems/minimum-number-of-refueling-stops/)。

reachable表示累计已选油量所能到达的最远位置。按题目已排序站表，把所有不超过该位置的站的油量放入最大堆。只有还到不了终点时才选一次加油；从可达站中取最大油量，使相同停靠次数下可达距离最大，不会比选择更少油的站损失后续机会。取出一个站后不再使用，堆空而终点不可达就无解。这个顺序表示规划哪些已途经站停靠，不是要求车倒退。

时间O(n log n)，额外空间O(n)，输入站表保持，恰好到站或终点允许剩余油量为0。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
