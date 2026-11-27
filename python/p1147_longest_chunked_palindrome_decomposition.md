# 1147. Longest Chunked Palindrome Decomposition · Python

[原题](https://leetcode.com/problems/longest-chunked-palindrome-decomposition/)。

分块回文要求从两端对应的整块字符串相同，目标是块数最多。从外向内寻找最短相同前后缀，找到就立刻切出一对并继续处理内部。最优方案若用了更长外块，可以在两端沿这个更短匹配块细分而不减少块数，因此选择最早匹配是安全的。扫描结束后，未匹配剩余部分或单独中心字符合成一个中块。例如aaaa可拆四块，abc只能作为一块。

字符串累加和比较最坏时间O(n^2)，额外空间O(n)，不使用有碰撞风险的哈希。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
