# 868. Binary Gap · Python

[原题](https://leetcode.com/problems/binary-gap/)。

从最低位向最高位查看，遇到1就与上一个1的位下标作差，并更新上次位置。只比较相邻1，两个1之间的0个数比所求距离少1，不能混用。不到两个1时没有合法配对，答案保持0。右移只更新函数局部整数。

时间O(log n)，额外空间O(1)，按整数位操作计。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
