# 1201. Ugly Number III · Python

[原题](https://leetcode.com/problems/ugly-number-iii/)。

本题丑数指能被a、b、c至少一个整除，不是只有这三个素因子的乘积。通过两两和三者最小公倍数容斥得到<=bound的精确个数，避免重复计入公倍数。该个数单调不减，二分最小使count>=n的bound即第n个数。上界n*min(a,b,c)包含至少n个最小除数的倍数，始终安全。Python整数不溢出。

有界整数模型下时间O(log(n*min(a,b,c)))，额外空间O(1)。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
