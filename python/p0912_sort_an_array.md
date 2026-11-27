# 912. Sort an Array · Python

[原题](https://leetcode.com/problems/sort-an-array/)。

从长度1的有序段出发，每轮把相邻两个至多width长的段合并到另一缓冲区；两段各有游标，每次取较小头元素，等值取左段保持稳定。轮末交换源与缓冲角色并将段长翻倍，未满整段的尾部按实际边界合并。最终段长覆盖整个数组即完成，不调用内置排序，也不递归切片。

最坏时间O(n log n)，额外空间O(n)，返回副本，原数组保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
