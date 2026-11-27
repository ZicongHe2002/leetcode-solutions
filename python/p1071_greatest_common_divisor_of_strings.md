# 1071. Greatest Common Divisor of Strings · Python

[原题](https://leetcode.com/problems/greatest-common-divisor-of-strings/)。

若两串都由同一基元重复，交换拼接顺序不改变结果；反之非空字符串拼接可交换就具有共同重复基元。先排除不相等拼接，剩余情况下共同因串长度必须同时整除两长度，取长度gcd的前缀即最长共同因串。不能只取长度gcd而跳过内容兼容判断。

长度N、M，时间O(N+M)，拼接比较临时空间O(N+M)，输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
