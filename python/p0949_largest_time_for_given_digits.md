# 949. Largest Time for Given Digits · Python

[原题](https://leetcode.com/problems/largest-time-for-given-digits/)。

四个给定数字各使用一次，最多24个位置排列，直接构造小时和分钟检查24小时制边界。用距午夜分钟数比较大小，保存最大合法候选。输出固定两位小时和分钟，保留前导0；没有合法候选返回空串。重复数字产生重复候选不影响最大值，也不会漏用重复次数。

固定四数字下时间和额外空间O(1)，原数组保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
