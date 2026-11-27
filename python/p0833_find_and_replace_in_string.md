# 833. Find And Replace in String · Python

[原题](https://leetcode.com/problems/find-and-replace-in-string/)。

所有替换位置都相对于原字符串，必须先用原串判断source是否匹配，只记录成功的替换。然后扫描原下标，遇到成功起点输出target并跳过原source长度，否则输出原字符。题目保证有效替换区间不重叠，因此跳过不会遗漏另一个有效起点。不按替换后字符串重新匹配，也不要求indices预先有序。

设原长N、全部source总长S、输出长T，期望时间O(N+S+T)，额外空间O(替换数+N+T)，输入不修改。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
