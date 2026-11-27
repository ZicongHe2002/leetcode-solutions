# 1614. Maximum Nesting Depth of the Parentheses · Python

[原题](https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/)。

原题s长1..100，只含数字、加减乘除运算符及左右括号，并保证是合法括号字符串。求最大嵌套层数int；非括号字符不增加深度，不在本题额外解析算术或处理非法括号。

depth是当前前缀尚未闭合的左括号数，左括号加1、右括号减1，best记录经过的最大值。合法性保证depth不会为负并最终回到0；任意嵌套层数恰等于该位置包含的未闭合左括号数，所以前缀最大值就是答案。时间O(n)，额外空间O(1)。

独立参考按括号语法分解首个完整分量，深度为max(1+内层深度,后续拼接深度)，不直接取线性扫描中的最大余额。枚举0..7对括号的626个合法结构，每个加上数字0形成合法非空VPS；另测100长度、50层嵌套、无括号数字/运算符和原题混合表达式，核对int。

A使用OpenAI Codex辅助编写；实际验证见日志，未向LeetCode提交。提交后须由B正式review；仅按真实内容署名。
