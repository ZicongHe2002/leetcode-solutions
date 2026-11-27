# 996. Number of Squareful Arrays · Python

[原题](https://leetcode.com/problems/number-of-squareful-arrays/)。

相邻值之和需为完全平方数，先用整数平方根为所有不同值建立有向可接关系。排列状态只需末值与各值剩余次数，每次从可接且仍有次数的值中选一种，减一次后递归；没有剩余值形成一种完整排列。相同值按频次操作，不给不可区分的同值下标乘排列数。每种首值也只尝试一次，缓存合并相同剩余状态。

U种不同值、实际缓存状态S，复制频次元组的时间上界O(U^2 S+U^2)，空间O(US+U^2)，不是声称状态数为多项式。输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
