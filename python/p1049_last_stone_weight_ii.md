# 1049. Last Stone Weight II · Python

[原题](https://leetcode.com/problems/last-stone-weight-ii/)。

两石相减可看成给原石重量分配正负号，最小残重等价于将全部石头分两组、最小化组和差。只找不超过总和一半的最大可达子集和s，答案为total-2s。0/1背包从容量高到低更新，确保每块石头最多选一次；选择空子集总可达，单石和无法平衡情况自然覆盖。本题可自由选碰撞对，不能用1046强制最重碰撞的堆贪心代替。

N块总重S，时间O(NS)，空间O(S)，输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
