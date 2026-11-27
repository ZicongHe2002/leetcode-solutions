# 828. Count Unique Characters of All Substrings of a Given String · Python

[原题](https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/)。

某字符一次出现位置i，上一次为p、下一次为q。包含i且不含其他同字符的子串，左端可选p+1..i，右端可选i..q-1，共(i-p)*(q-i)个。扫描时保存每字符前两次位置，遇到新位置就结算中间一次；末尾以字符串长度作为每字符最后一次的下一位置补算。不存在的前次位置用-1。每个子串中每个唯一字符都按这一次出现计入，故贡献总和就是答案。

时间O(n)，额外空间O(U)，U为不同字符数。原题大写字母使U最多26。输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
