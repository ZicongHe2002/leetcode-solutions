# 898. Bitwise ORs of Subarrays · Python

[原题](https://leetcode.com/problems/bitwise-ors-of-subarrays/)。

以当前下标结尾的非空子数组，要么只有当前值，要么把上一位置结尾的子数组延长一项，所以新集合是{value}与所有旧或值|value。汇总到全局集合即可。固定右端向左扩展时，或值只会把0位变1，每次不同值至少新增一位，因此每个结尾不同值数量受整数位宽限制，不必保存全部起点。

设非负输入最大位宽W至少为1，时间O(nW)，全局集合空间上界O(nW)，结尾集合O(W)，按位运算在题目有界整数下计常数。输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
