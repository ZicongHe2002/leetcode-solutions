# 1016. Binary String With Substrings Representing 1 To N · Python

[原题](https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/)。

每个正整数的规范二进制表示以1开头，前导0不需要额外考虑。从s每个1位置出发，最多读取n的二进制位宽，逐位更新值并收集不超过n的结果；一旦超过n，继续追加位不会减小值，可以停止。集合内只含1..n，大小等于n就意味着全部覆盖。不循环遍历可能极大的1..n。

s长L、n位宽B，时间O(LB)，空间O(min(n,LB))，按题目有界整数计，输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
