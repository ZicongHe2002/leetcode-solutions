# 981. Time Based Key-Value Store · Python

[原题](https://leetcode.com/problems/time-based-key-value-store/)。

题目保证set时间严格递增，因此每个key追加的时间表自动有序，值表与之同下标。get用bisect_right找到第一个更晚时间，其前一项就是不晚于查询的最新值；恰好同时间的记录会被接受。key不存在或所有记录都晚于查询时返回空串，不创造虚假历史值。

set摊还O(1)，某key有M条历史时get为O(log M)，全部存储空间O(记录总数)，字符串引用按题目接口保存。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
