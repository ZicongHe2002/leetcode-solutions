# 1067. Digit Count in Range · Python

[原题](https://leetcode.com/problems/digit-count-in-range/)。

先求正整数1..bound内数字d的总出现次数，再用high前缀减low-1前缀。每个数位状态返回可完成的正整数方案数和后缀d次数；当前有效数字若为d，就给每个后缀方案再加一次。started区分尚未开始的前导0与真实内部0，前导占位不计，结束全未开始也不算正整数。题目区间从正整数开始，bound<=0时前缀计数0。

L位上界，位置、tight、started仅O(L)个状态，每态枚举10数字，时间O(10L)，空间O(L)，不逐整数扫描区间。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
