# 1079. Letter Tile Possibilities · Python

[原题](https://leetcode.com/problems/letter-tile-possibilities/)。

题目最多7块字母砖。每层只按字母种类选择一次，扣减频次后，新前缀本身贡献1，随后递归统计它的所有更长扩展，再恢复频次。每个不同字符串对应唯一字母选择路径，不会因两块相同字母砖的身份产生重复。比如AA只有A、AA两种非空字符串。

设非空可构造前缀数为P、不同字母数为K，时间O(K(P+1))，P不超过所有长度排列数之和O(n!)，额外空间O(n+K)，输入不修改。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
