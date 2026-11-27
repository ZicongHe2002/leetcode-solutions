# 903. Valid Permutations for DI Sequence · Python

[原题](https://leetcode.com/problems/valid-permutations-for-di-sequence/)。

ways[r]表示当前前缀排列末项在已使用元素中的排名为r的方案数。加入新末项，其排名为j：I要求旧末项在插入前排名小于j，故新计数是旧ways[:j]之和；D要求旧排名至少j，故是ways[j:]之和。新排名有旧长度加1种，分别用正向前缀和或反向后缀和一次算全。初始单元素只有排名0一种，最终对所有末排名求和。

关系串长N，时间O(N^2)，滚动数组额外空间O(N)，按10^9+7取模，输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
