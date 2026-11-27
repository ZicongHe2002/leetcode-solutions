# 896. Monotonic Array · Python

[原题](https://leetcode.com/problems/monotonic-array/)。

非递减要求每个相邻对前项不大于后项，非递增要求相反。初始两种方向都可能，每出现一次下降就排除非递减，每出现一次上升就排除非递增。相等不排除任何方向，因此常量数组和单元素数组都单调。两方向同时被排除可立即返回False。

时间O(n)，额外空间O(1)，不排序也不修改输入。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
