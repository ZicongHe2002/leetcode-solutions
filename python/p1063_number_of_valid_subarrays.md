# 1063. Number of Valid Subarrays · Python

[原题](https://leetcode.com/problems/number-of-valid-subarrays/)。

有效子数组要求首项不大于其中任何元素。读到当前值后，所有仍等待的首项若大于它，就不可能再作为跨过当前处的合法起点，单调栈弹去这些较大首值；其余起点仍合法，再加入当前单元素起点。栈每项代表一个实际起点，重复相等值要分别保留，因此当前栈长就是以该处结束的有效子数组数。

每项入出栈一次，时间O(n)，额外空间O(n)，输入不修改。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
