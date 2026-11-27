# 1169. Invalid Transactions · Python

[原题](https://leetcode.com/problems/invalid-transactions/)。

金额严格超过1000，或存在同名、异城且时间差不超过60分钟的另一笔交易，即为无效。逐笔比较全部记录，每个原始下标独立判定，避免用字符串集合去重而漏掉重复条目。时间差取绝对值，输入不必有序；恰好60分钟仍冲突，恰好1000金额本身不违规。

按题目有界字段长度，时间O(n^2)，额外空间O(n)，输出保持原始交易文本。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
