# 1085. Sum of Digits in the Minimum Number · Python

[原题](https://leetcode.com/problems/sum-of-digits-in-the-minimum-number/)。

输入为非空正整数数组。先取最小值，再反复取个位并去掉个位，最后按题意返回数字和的偶数标志。例如最小值为23时，数字和为5，返回0；不能用最小值自身的奇偶性代替数字和的奇偶性。

数组长n，最小数有D位，时间O(n+D)，额外空间O(1)，不修改数组。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
