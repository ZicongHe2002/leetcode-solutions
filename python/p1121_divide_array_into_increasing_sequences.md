# 1121. Divide Array Into Increasing Sequences · Python

[原题](https://leetcode.com/problems/divide-array-into-increasing-sequences/)。

输入已按非降序排列，需要分成严格递增且每条至少k项的子序列。设某值最多重复m次，它们必须进入不同序列，所以至少需要m条，每条k项给出必要条件n>=mk。这个条件也充分：把有序数组按下标模m轮流分到m条，同值连续段长度最多m，不会在同一条重复；每条长度至少floor(n/m)>=k。只需扫描相等连续段得到m。

时间O(n)，额外空间O(1)，无需实际构造序列，不修改输入。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
