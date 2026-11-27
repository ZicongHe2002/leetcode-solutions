# 1175. Prime Arrangements · Python

[原题](https://leetcode.com/problems/prime-arrangements/)。

排列1..n，所有素数必须放在编号为素数的位置。设素数个数P，素数值与素数位置恰有P个，可作P!种双射，其余位置由非素数作(n-P)!种排列，两者独立相乘。1不是素数，n至少1；筛法从p^2开始删除倍数，并在阶乘过程中取模10^9+7。

时间O(n log log n)，额外空间O(n)，无需枚举所有排列。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
