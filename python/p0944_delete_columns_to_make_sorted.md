# 944. Delete Columns to Make Sorted · Python

[原题](https://leetcode.com/problems/delete-columns-to-make-sorted/)。

本题要求每个保留列单独从上到下非递减，各列互不影响。某列只要存在相邻逆序就不能保留，删除其他列无法改变它；若没有相邻逆序，传递性保证整列有序。逐列统计坏列即为最少删除数，等值允许保留，只有一行时没有坏列。

R行C列，时间O(RC)，额外空间O(1)，输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
