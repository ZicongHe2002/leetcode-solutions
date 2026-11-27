# 900. RLE Iterator · Python

[原题](https://leetcode.com/problems/rle-iterator/)。

编码交替保存次数和值，初始化复制编码保护调用方数组。next(n)若当前游程不足，就扣去其全部剩余数并前进两格；否则当前游程足够，减去n后返回其值。恰好耗完仍应返回本次最后消耗的值，下一次调用才跨过剩余0的游程。零次数段会直接跳过，全部耗尽返回-1，不展开巨大原序列。

R个游程、Q次调用，游程游标总共只前进R次，总时间O(R+Q)，单次最坏O(R)，复制存储O(R)。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
