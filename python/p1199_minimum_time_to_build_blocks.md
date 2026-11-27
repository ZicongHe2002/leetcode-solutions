# 1199. Minimum Time to Build Blocks · Python

[原题](https://leetcode.com/problems/minimum-time-to-build-blocks/)。

初始一个工人，每个工人可花split时间分成两个工人，之后两支可并行。把工作计划看成分工二叉树，两个子任务合成一个上层任务耗时为split+max(两者)。较短任务可安排在更深层而不增加整体完工时间，最短两个任务可作为最深兄弟，因此重复合并堆中最短两个值得到最优计划。单个块无需分工，直接返回其建造时间。

时间O(n log n)，额外空间O(n)，原blocks不修改。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
