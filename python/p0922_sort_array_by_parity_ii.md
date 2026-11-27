# 922. Sort Array By Parity II · Python

[原题](https://leetcode.com/problems/sort-array-by-parity-ii/)。

题目保证偶数奇数各占一半。偶下标已经放偶数就保留，否则在奇下标游标处寻找放错的偶数，与之交换，两处同时满足要求。两指针只向前，不会重复检查已归位位置；两类数量相等保证每个偶下标错位都能找到对应奇下标错位。

时间O(n)，结果副本O(n)，除输出外额外空间O(1)，原数组保持，同类顺序不作保证。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
