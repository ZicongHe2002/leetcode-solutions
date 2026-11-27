# 1064. Fixed Point · Python

[原题](https://leetcode.com/problems/fixed-point/)。

数组严格递增且为整数，相邻值至少增1，所以arr[i]-i非递减。二分首个差不小于0的位置；若该处差为0，就是最小不动点，否则此前差都负、之后差都正或更大，不存在解。必须找下界而非遇到任一相等就返回，因为可能多个连续下标都满足。越界也返回-1。

时间O(log n)，额外空间O(1)，输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
