# 1072. Flip Columns For Maximum Number of Equal Rows · Python

[原题](https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/)。

同一组列翻转要使两行各自所有位相等，则两行原模式必须完全相同或逐位互补。每行与自身首位异或，将首位统一为0，恰好把相同与互补行映射为同一键。选择某键对应的翻转后，该组原行会各自成为全0或全1，两种都满足题意，因此最大键频次就是答案。不要求所有成功行最终互相相同。

R行C列，期望时间O(RC)，模式键空间O(RC)，原矩阵保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
