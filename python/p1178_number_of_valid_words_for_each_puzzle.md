# 1178. Number of Valid Words for Each Puzzle · Python

[原题](https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/)。

单词有效当且仅当字母集合是谜题字母集合的子集，并包含谜题首字母；字母出现次数不影响有效性，但重复单词各自计数。每个谜题有七个不同字母，固定首字母后只需枚举其余六位的64个子集，避免逐谜题扫描全部单词。超过七种字母的单词不可能有效，预处理时直接跳过。空子集仍需计入，它对应只包含首字母的一类词。

单词总字符数L、谜题数P，时间O(L+64P)，额外空间O(D+P)，D为保留掩码数。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
