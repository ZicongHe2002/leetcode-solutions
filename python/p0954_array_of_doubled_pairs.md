# 954. Array of Doubled Pairs · Python

[原题](https://leetcode.com/problems/array-of-doubled-pairs/)。

按绝对值递增处理，使非零值的双倍总在更后面，不论正负。当前仍剩的x不能再被更小绝对值消耗，只能各配一个2x，检查频次并批量扣除；若不足就不可能配全。0的双倍仍为0，必须偶数个才能两两配对，不能用普通自扣频次跳过奇数零的错误。只修改频次副本。

N项U种值，时间O(N+U log U)，额外空间O(U)，原数组保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
