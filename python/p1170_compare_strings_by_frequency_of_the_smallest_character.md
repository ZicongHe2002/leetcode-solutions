# 1170. Compare Strings by Frequency of the Smallest Character · Python

[原题](https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/)。

所有字符串非空，f(s)定义为字典序最小字符的频次，不是最大字符频次或最小频次数。先把words变成有序频次数组，查询f(query)的右边界，后方元素都严格更大；相等频次不会计入。每个字符串先取最小字符再count，线性扫描其内容即可。

总字符数L、词数W、查询数Q，时间O(L+W log W+Q log W)，额外空间O(W+Q)。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
