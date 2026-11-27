# 1208. Get Equal Substrings Within Budget · Python

[原题](https://leetcode.com/problems/get-equal-substrings-within-budget/)。

两串等长，位置i的转换代价为字符编码差绝对值，所有代价非负。右端每前进一步加入新代价，超预算时左端逐步右移直到恢复可行，此时为当前右端的最长可行窗口。预算恰好用完仍合法，maxCost=0时只能保留零成本区间。

每个位置至多进入和移出一次，时间O(n)，额外空间O(1)，两字符串保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
