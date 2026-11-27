# 1012. Numbers With Repeated Digits · Python

[原题](https://leetcode.com/problems/numbers-with-repeated-digits/)。

直接数至少重复一次较复杂，改数没有重复位的正整数，再从1..n的n个数中扣掉。状态记录位置、已用数字位掩码、是否仍贴住上界以及是否已开始有效数字。尚未开始的0只是前导占位，不加入掩码；开始后的0与其他数字一样不能重复。结束只计已开始的数，排除0。tight分支限制当前数字不超过n对应位，其余分支可选0..9。

n有L位，时间O(L*2^10*10)，缓存空间O(L*2^10)，不逐个遍历1..n。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
