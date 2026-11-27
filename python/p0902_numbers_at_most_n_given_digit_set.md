# 902. Numbers At Most N Given Digit Set · Python

[原题](https://leetcode.com/problems/numbers-at-most-n-given-digit-set/)。

可用数字均为1..9，所以任何长度更短的拼接都是合法正整数，长度l有D^l种。与n同长时，从左向右保持此前前缀相等，当前位选比n该位小的允许数字后，剩余位任意选择；这些方案按首次更小位置互不重叠。若当前n数字不在集合，相等前缀无法继续，立即返回。全部位都能相等时再加入n本身。

设n有L位、允许数字D个，按整数算术计时间O(LD+L^2)，包含逐次幂运算的保守上界，额外空间O(L+D)，输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
