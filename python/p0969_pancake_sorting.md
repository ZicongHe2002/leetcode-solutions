# 969. Pancake Sorting · Python

[原题](https://leetcode.com/problems/pancake-sorting/)。

输入是1..n的排列。已把更大值归位后，值length就是当前剩余前缀的最大值，若已在末位就跳过；否则先翻到首位，再翻整个剩余前缀，把它固定到正确末位。后续更短翻转不再影响已归位后缀，每轮至多两次，总操作数至多2(n-1)，低于题目10n限制。只在副本模拟，返回的是操作长度而不是排序数组。

时间O(n^2)，副本、切片与结果空间O(n)，原数组保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
