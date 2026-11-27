# 1184. Distance Between Bus Stops · Python

[原题](https://leetcode.com/problems/distance-between-bus-stops/)。

distance[i]是站i到(i+1)%n的路段长度，允许沿环两种方向乘车。将两个站编号排成first<=last，累加[first,last)路段得到一侧距离，另一侧为总环长减去该值，取较小者。相同起终点对应空区间，返回0。

时间O(n)，额外空间O(1)，不切片、不修改原路段数组。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
