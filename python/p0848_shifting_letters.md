# 848. Shifting Letters · Python

[原题](https://leetcode.com/problems/shifting-letters/)。

第i次操作移动前i+1个字符，所以位置j会受到所有i>=j的操作影响，恰为shifts的后缀和。逆序扫描维护该累计量，每步按26取模；字符转为0..25索引，加累计量再取模转回小写。移位可加且模运算相容，不必真的重复修改每个前缀。

时间O(n)，结果空间O(n)，除结果外额外空间O(1)，shifts和原字符串不修改。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
