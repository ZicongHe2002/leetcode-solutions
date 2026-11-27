# 906. Super Palindromes · Python

[原题](https://leetcode.com/problems/super-palindromes/)。

超级回文既是回文数，也是某个回文正整数的平方。用整数平方根把原闭区间转为平方根闭区间，避免浮点边界误差。每个正整数前缀分别镜像生成奇位与偶位回文；两类长度不同，不重复。只对根在范围内的候选检查平方文本回文。奇位候选随种子递增，且同种子的偶位候选更大，因此奇位根超过上界时可以停止两类枚举。

设生成P个种子、原上界为R，时间O(P log R)，额外空间O(log R)，按整数运算计；没有逐个扫描所有平方根。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
