# 1017. Convert to Base -2 · Python

[原题](https://leetcode.com/problems/convert-to-base-neg2/)。

低位必须为0或1，按奇偶选bit=n&1，再由n=下一商*(-2)+bit得到下一商。即使中间商为负数，n-bit仍是偶数，整除-2没有余数歧义。逐低位记录再反转，结束的最后一个高位必非0；原数0单独输出0。不使用正二进制字符串简单改符号。

时间与结果空间O(log(n+2))，除结果外整数状态O(1)。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
