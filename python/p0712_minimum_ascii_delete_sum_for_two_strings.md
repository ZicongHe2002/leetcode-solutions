# 712. Minimum ASCII Delete Sum for Two Strings · Python

[原题](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/)。

原题s1、s2各长1..1000，只含小写英文，删除字符的代价为其ASCII码，求使两串相等的最小总代价。比较的是代价总和而非删除字符数量。字符串保持；额外支持空串，需删除另一串的全部字符。

cost[j]表示两个当前前缀变为相同的最小代价。初始行是删除s2前缀的累计代价；每一行首列加上当前s1字符的代价。尾字符相等可直接接在前缀共同结果后，取旧对角；不等则必删其中一端，取旧同列删s1字符与新前列删s2字符的较小值。diagonal在覆盖前保存旧同列，供下一列使用。时间O((len(s1)+1)*(len(s2)+1))，额外空间O(len(s2)+1)。

独立oracle显式枚举两串的全部子序列集合，找共同子序列中ASCII和最大的一个，再用两串总代价减两倍保留代价，不复用删除DP。二字母串各长0..4共961对核对，空串为扩展。边界覆盖1000字符、不同字符的权重、相反双块与只差一个字符，核对int。

A使用OpenAI Codex辅助编写；实际验证见日志，未向LeetCode提交。提交后须由B正式review；仅按真实内容署名。
