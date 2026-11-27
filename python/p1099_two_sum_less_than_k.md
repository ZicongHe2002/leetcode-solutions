# 1099. Two Sum Less Than K · Python

[原题](https://leetcode.com/problems/two-sum-less-than-k/)。

输入为正整数数组，必须使用两个不同下标，并要求和严格小于k。排序后，若当前和过大，固定右端时更大的左端都不可行，所以缩小右端；若当前和可行，它已是当前左端与剩余右端组合中的最大值，记录后增大左端。双指针只在left<right时运行，找不到合法配对返回-1，相等于k的和不会被接受。

时间O(n log n)，额外空间O(n)，使用排序副本保持输入数组。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
