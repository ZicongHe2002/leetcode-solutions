# 905. Sort Array By Parity · Python

[原题](https://leetcode.com/problems/sort-array-by-parity/)。

两次按原顺序扫描，先收集全部偶数、再收集全部奇数并连接。每个输入值进入且仅进入一组，所以保持原元素及重复次数；同组相对顺序也保留，虽然题目不强制稳定。0属于偶数，输入不修改。

时间O(n)，新列表及拼接结果总额外空间O(n)。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
