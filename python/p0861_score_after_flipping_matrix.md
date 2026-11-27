# 861. Score After Flipping Matrix · Python

[原题](https://leetcode.com/problems/score-after-flipping-matrix/)。

每行最高位权重大于该行所有低位权重之和，所以可令每行最高位为1：最高位0的行整体翻转。无需实际改格，翻转后其他位置为1恰当且仅当原位等于原最高位。随后每列可独立翻转，选择让1数量为ones与行数-ones中的较大者，乘对应二进制位权累计。

时间O(RC)，额外空间O(1)，不修改输入矩阵。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
