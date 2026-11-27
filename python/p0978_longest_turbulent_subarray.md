# 978. Longest Turbulent Subarray · Python

[原题](https://leetcode.com/problems/longest-turbulent-subarray/)。

up表示到当前处最后一条边上升的最长严格交替段，down表示最后下降。新边上升只能接此前下降段，反之亦然；另一个方向状态退回单元素长度1。相邻相等不能参与严格波动，两态都重置1。用同时赋值读取旧状态，每步更新历史最长值，非空单元素答案为1。

时间O(n)，额外空间O(1)，输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
