# 967. Numbers With Same Consecutive Differences · Python

[原题](https://leetcode.com/problems/numbers-with-same-consecutive-differences/)。

多位数首位不能为0，从1..9开始逐位扩展。末位为d时，下位仅可能d-k或d+k，过滤0..9之外的值即可穷尽合法后继。用集合列出两个候选，k=0时只追加一次，不产生重复答案。每轮前缀唯一且新数有唯一前缀，所以其他情况也不会重复。单数字长度另含合法数字0。

分支最多2，保守时间上界O(n*2^n)，结果与滚动候选空间O(2^n)，按题目有界整数计，输入参数不含可变制品。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
