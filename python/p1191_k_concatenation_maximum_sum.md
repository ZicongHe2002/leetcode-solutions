# 1191. K-Concatenation Maximum Sum · Python

[原题](https://leetcode.com/problems/k-concatenation-maximum-sum/)。

允许空子数组，因此最大值至少0。k=1只需Kadane；k>=2时，两份数组已覆盖单份内部区间以及后缀连接前缀的跨界区间。若整份总和为正，可在跨界两端之间插入k-2份完整数组；总和非正则插入完整副本没有收益。仅在取得真实最大和之后取模，不能把中间比较值先取模。

时间O(n)，额外空间O(1)，不实际复制k份数组。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
