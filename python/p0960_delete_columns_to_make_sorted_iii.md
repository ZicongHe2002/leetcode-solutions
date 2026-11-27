# 960. Delete Columns to Make Sorted III · Python

[原题](https://leetcode.com/problems/delete-columns-to-make-sorted-iii/)。

此题要求每一行保留后的字符都非递减，且所有行删除同一组列。列j能接在列i后，当且仅当i<j且每一行该处字符都满足row[i]<=row[j]。把这个共同兼容关系作为最长子序列转移，longest[j]保存以j结束的最多保留列数，总列数减最大保留数就是最少删除。不能套用955只比较相邻整行字典序的贪心。

R行C列，时间O(RC^2)，额外空间O(C)，输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
