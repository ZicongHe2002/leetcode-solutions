# 910. Smallest Range II · Python

[原题](https://leetcode.com/problems/smallest-range-ii/)。

每项必须选择加k或减k。排序后只需枚举某个分界前统一加、之后统一减：若较小值减而较大值加，会向外拉开，把这对方向改成向内不会扩大原有范围，可消除这种交错。固定分界后，最大值来自加k前缀末项或减k后缀末项，最小值来自前缀首项或后缀首项。全部同方向时范围仍为原极差，作为初始候选，单元素也自然为0。

时间O(n log n)，排序副本额外空间O(n)，原数组保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
