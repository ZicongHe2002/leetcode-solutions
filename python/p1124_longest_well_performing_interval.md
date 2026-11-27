# 1124. Longest Well-Performing Interval · Python

[原题](https://leetcode.com/problems/longest-well-performing-interval/)。

只有严格超过8小时才算劳累日，将它映射为+1，其他为-1，目标区间和严格大于0。当前前缀和正时，从起点到当前就是最长候选；否则寻找最早的score-1前缀即可。前缀每次只变1，任何更小前缀在首次达到前都必经score-1，所以最早score-1不会比其他可行更小前缀更晚，能给出最长区间。每个前缀值只保存首次位置，初始0位于-1，不能覆盖为更晚的位置。

期望时间O(n)，额外空间O(n)，输入工时数组保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
