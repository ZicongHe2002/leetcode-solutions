# 830. Positions of Large Groups · Python

[原题](https://leetcode.com/problems/positions-of-large-groups/)。

start是当前连续段首位，end向右寻找首个不同字符或字符串末尾，得到半开区间[start,end)。长度至少3时按题目要求输出闭区间[start,end-1]，再从end开始下一段。每段只产生一次结果，天然按起点递增，末尾段也会被处理。

时间O(n)，除输出外额外空间O(1)，输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
