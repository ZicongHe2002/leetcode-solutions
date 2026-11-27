# 1074. Number of Submatrices That Sum to Target · Python

[原题](https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/)。

固定上下边界后，每列在这两行之间的和形成一维数组，任一连续列段恰对应一个矩形。向下扩展bottom时增量更新列和，再用前缀频次：当前prefix需要此前prefix-target即可组成目标和区间，查询后才加入当前前缀，避免空区间。每对上下边界独立建频次表，负数与0都支持，不使用正数滑窗。

R行C列，时间O(R^2 C)，额外空间O(C)，不修改原矩阵。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
