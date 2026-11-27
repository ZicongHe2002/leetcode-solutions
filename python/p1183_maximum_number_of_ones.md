# 1183. Maximum Number of Ones · Python

[原题](https://leetcode.com/problems/maximum-number-of-ones/)。

题目sideLength不超过矩阵两维，任意sideLength正方形最多maxOnes个1。按行列模sideLength划分位置类型，每个完整正方形恰好包含每种类型一次。选定某些类型并周期性填1，即可让每个窗口的1数恰等于所选类型数。某类型在全矩阵出现次数为对应行数乘列数，按完整块与边界条带分配可知，最大总数的上界恰为最高maxOnes个重复次数之和，周期构造能达到该上界。maxOnes为0时自然返回0，不实际建立大矩阵。

令S=sideLength，时间O(S^2 log S)，额外空间O(S^2)。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
