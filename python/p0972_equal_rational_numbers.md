# 972. Equal Rational Numbers · Python

[原题](https://leetcode.com/problems/equal-rational-numbers/)。

整数部分直接作分数，长度a的有限小数段值为其整数/10^a。长度b的循环节对应几何级数，贡献为循环节整数/(10^a*(10^b-1))，与前两部分相加。Fraction自动约分，因此0.(9)与1等价，不同循环节长度或重复写法也按实际数值比较。空有限小数段和全0循环节自然处理，不截断浮点近似。

原题各数字段长度有固定小上限，时间和额外空间在该格式范围内为O(1)，实际运算是有限整数解析与分数化简。输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
