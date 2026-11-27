# 878. Nth Magical Number · Python

[原题](https://leetcode.com/problems/nth-magical-number/)。

能被a或b整除的正整数个数由floor(x/a)+floor(x/b)-floor(x/lcm(a,b))给出，最后一项消除共同倍数重复。该计数单调，以min(a,b)与n*min(a,b)界定第n个数的范围，二分最早达到n的位置；不能对计数过程先取模，否则单调性会丢失。只在得到实际第n个整数后按10^9+7取模。

时间O(log(n*min(a,b))+log(min(a,b)))，包含最大公约数，额外空间O(1)，按整数算术计。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
