# 1150. Check If a Number Is Majority Element in a Sorted Array · Python

[原题](https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/)。

数组已非降序排列，所有target连续。左边界为第一个不小于target的位置，右边界为第一个大于target的位置，两者之差就是精确出现次数。多数要求严格超过一半，不能把恰好一半算作多数；目标缺失时边界相等，次数0。

时间O(log n)，额外空间O(1)，不切片或修改输入。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
