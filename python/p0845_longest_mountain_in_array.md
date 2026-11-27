# 845. Longest Mountain in Array · Python

[原题](https://leetcode.com/problems/longest-mountain-in-array/)。

山脉必须先至少一条严格上坡边，再至少一条严格下坡边。up和down分别计当前两段边数。遇到相等值平台，两段都结束；已经下坡又上坡时，从当前谷底重新开始。只有up和down同时非0才更新长度up+down+1，因此纯升、纯降和平台都不会误算山脉。

时间O(n)，额外空间O(1)，输入不修改。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
